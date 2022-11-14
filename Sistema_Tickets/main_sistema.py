from funciones import*

#Declaro constantes, como lo son los valores de las entradas.
VALOR_VIP = 20000
VALOR_GENERAL = 15000

venta = 0
#Cartel de bienvenida al programa.
bienvenida()

#Elegimos una matriz de asientos 50 x 50.
filas = 50             
columnas = 50

#Comprueba si hubo una compra antes de realizar alguna acción en particular del menú. 
hubo_compra = False  

#Traemos la información de la 'Base de datos' y si no se encuentra el archivo, creamos uno.
matrizAsientos = (transformar_archivo('asientos.txt'))

matVentas = transformar_archivo_ventas('ventas.txt')

cont = cont_filas_ventas(matVentas)

n=menu()

while n >= 1 and n <= 13:
        
        num = num_ticket(cont_ticket(matrizAsientos))

        if n == 1:                
            #MUESTRO ASIENTOS DISPONIBLES 

            print("Disponibilidad de asientos: \n")
            printMatriz(matrizAsientos)

        elif n == 2:
            #Pido y verifico dispopnibilidad de asientos en la ubicación seleccionada, si está en sector VIP o General y si se ha agotado la totalidad de los asientos.
            f,c = 50,50                                  
            f,c = pedirAsiento(f, c)
            
            hay_asientos= asientosLibres(matrizAsientos,f,c)
            es_vip = vip(f)
            asientos_agotados = fullAsientos(matrizAsientos)

            if hay_asientos == True:
            
                if es_vip == True:
                    print("\nElegiste sector VIP ($20.000).\n\nConsultando disponibilidad. . .\n")
                    venta += 20000
                    monto = str(20000)
                    
                else:
                    print("\nEstás comprando asientos en sector General ($15.000).\n\nConsultando disponibilidad. . .\n")
                    venta += 15000
                    monto = str(15000)
                print("Hay asientos disponibles.\n")    
                                                  
                usuario, dni, edad = datos_compra()


            else:

                #Si los asientos están agotados, que salga del bucle para que luego pase a la siguiente condición y pueda seguir con el resto del programa.
                while hay_asientos == False:
                        
                        print("Asiento NO disponible, vuelve a intentar: \n") 
                        f = 50                    
                        c = 50
                        f,c = pedirAsiento(f, c)
                        hay_asientos = asientosLibres(matrizAsientos,f,c)
                        
                        if es_vip == True:
                            print("\nElegiste sector VIP ($20.000).\nConsultando disponibilidad. . .\n")
                            venta += 20000
                            monto = str(20000)

                        else:
                            print("\nEstás comprando asientos en sector General ($15.000).\nConsultando disponibilidad. . .")
                            venta += 15000

                usuario, dni, edad = datos_compra()

            #Verificamos que no se pueda comprar un asiento con el mismo DNI, a excepción de que tenga el mismo nombre de usuario.
            j = 0       
            while j <= cont:
                
                if j != cont:
                    
                    if matVentas[j][1] == dni and matVentas[j][0] == usuario:

                        j = cont
                        
                    elif matVentas[j][1] == dni and matVentas[j][0] != usuario:  
                        dni = input("El DNI pertenece a otro usuario, ingrese nuevamente el documento: ")
                        j = -1

                    while (not es_numero(dni)) or (len(dni) < 7 or len(dni) > 8):
                        print("\nIngrese únicamente números de 7 u 8 dígitos.")
                        dni = input("\nDNI: ") 

                        if matVentas[j][1] == dni and matVentas[j][0] == usuario:
                            j = cont

                        else:
                            j -=1    

                j += 1

            hubo_compra = True

            print("\nAsiento Asignado")   
            
            #Agregamos la compra del asiento a la matriz de los asientos y transformamos su respectivo tipo de dato para poder trabajar con el mismo sin errores.               
            matrizAsientos[f][c] = 1
            mat_transf = transformar(matrizAsientos)

            print("\nAsientos libres sector VIP:", end=" ")
            es_vip = vip(f)
            esta_lleno_vip = fullVip(matrizAsientos) 

            #Creamos y cargamos matriz de ventas que luego será transformada y actualizada al archivo de 'ventas.txt'
            lista_ventas =[usuario, dni, edad, f, c]
            matVentas.append(lista_ventas)                   

            #Contador de ventas realizadas (Actualizada de los archivos) y número de ticket actual.
            cont += 1   
            numventas=cont_ticket(matrizAsientos) + 1

        elif n == 3:              

            #Generación de archivo Ticket. (Si se ha efectuado una compra anteriormente).
            if hubo_compra == True:

                print("\nHa decidido imprimir un ticket\n")

                try:

                    if num != '0000':    
                        print("Número de Ticket: '" + str(num)+ "'")
                        fd = open('ticket_' + num  + '.txt', 'w')
                        fd.write('TICKET DE COMPRA N°' + num +'\nUsuario: '+ usuario+'\nDni: ' + dni + '\nAsiento reservado: F{' + str(f) +'} A{' + str(c) + '}' + '\nedad: '+ edad)
                        
                        if es_vip==True:
                            fd.write("\nValor de compra (VIP): $" + str(VALOR_VIP))

                        else:
                            fd.write("\nValor de compra (GENERAL): $" + str(VALOR_GENERAL))     
                        fd.close()  

                        num = int(num)
                        num += 1
                        num = str(num)

                except NameError:    
                    print("\nNo has ingresado los datos de compra aún... Vuelve a ingresar nuevamente\n")  

                hubo_compra == False 

            else: 
                print("\nNecesita generar una venta antes de crear un ticket . . .\n")

            hubo_compra == False 

        elif n == 4:

            #Guardamos y actualizamos la matriz de Ventas al archivo 'ventas.txt'
            matVentasT = transformar(matVentas)

            try:  
                fd = open('ventas.txt', 'w')

                for fila in matVentasT:
                    fd.write(fila + '\n') 

                fd.close()      

            except FileNotFoundError:  

                fd = open('ventas.txt', 'w')

                for fila in matVentasT:
                    fd.write(fila + '\n')  

                fd.close()  
 

            out = salida()   

            if out == True:
                n = 0  

        elif n == 5:
            
            #Buscar usuarios y mostrar su ticket por pantalla en caso de pérdida de ticket.
            user_search= input("\nIngrese el usuario para buscar su asiento: ")
            user_search= buscarUsuarios(user_search, matVentas)

        elif n == 6:

            #Se busca, muestra y ordena alfabeticamente los nombres de los usuarios junto a sus respectivos datos de venta. 
            try: 
                matriz_ordenada = burbujeo_vip(matVentas)

                print_venta = imprimir_venta_vip(matriz_ordenada)    

            except TypeError:
                print(end="")        

        elif n == 7:

            #Generamos un promedio de edades para cada sector.
            promedioGral, promedioVip = promedio_edad(matVentas)
            print("\nPromedio de edades en el sector General: " + str(promedioGral) + ' Años.\n\nPromedio de edades en el sector VIP: ' + str(promedioVip) + ' Años.')

        elif n == 8:

            #En caso de pérdida de ticket, buscar en los archivos y mostrar su ticket por pantalla.
            lost_ticket=input("\nIngrese número de ticket para visualizar: N°")
            lost_ticket = buscar_ticket(lost_ticket)

        elif n == 9:

            #Mostrar por pantalla cuánto se ha generado hasta la fecha por ventas de tickets (Ambos sectores).
            recaudacionTotal = recaudacion(matVentas)
            print("\nRecaudación total hasta la fecha: $" + str(recaudacionTotal))

        elif n == 10:

            #Mostrar por pantalla los usuarios menores de 21 años y ordenarlos alfabéticamente.
            try:

                lista_usuarios21 = usuarios_u21(matVentas)
                print("\nLista de usuarios menores de 21 años: ", list_to_str_comas(lista_usuarios21), "\n")

                lista_ord_21 = burbujeo(lista_usuarios21)
                print("\nLista de usuarios menores de 21 años en orden Alfabético: ",list_to_str_comas(lista_ord_21),"\n")

            except TypeError:

                print("\nNo se han cargado usuarios menores de 21 años al sistema.\n")

        elif n == 11:

            #compras con dni ordenadas de manera Descendente.
            mat_dni = burbujeo_general(matVentas)
            imprimir_venta_dni(mat_dni)

        elif n == 12:
            
            matriz_sorteo = mat_filas_sorteo(matVentas)

            sector = sorteo(matriz_sorteo, matVentas)

            try:
                if sector == True:
                    recaudacionTotal -= VALOR_VIP
                else:
                    recaudacionTotal -= VALOR_GENERAL
            except NameError:
                print("\nNecesita haber visualizado o cargado la recaudación total hasta el momento...\nSeleccionando 9 puede solucionarlo!\n")

        elif n == 13:
            #Opción de salida del sistema para el usuario.
            out = salida()

            if out == True:
                n = 0    

        if n != 0:
            
            #Si el usuario desea continuar, se volverá a mostrar el menú.
            n = menu()
            #compras con dni ordenadas.

#Se cargan los datos en el archivo 'asientos.txt' al finalizar el día.
matrizAsientos = transformar(matrizAsientos)

fd = open("asientos.txt", 'w')
fd.write(" "*(filas) + 'COLUMNAS\n')
numero_f = 0
for fila in matrizAsientos:
    fd.write("Fila["+ str(numero_f)+'] ' + fila +'\n')
    numero_f +=1
fd.close()   


#Se carga la información en el archivo 'ventas.txt' al finalizar el día.
matVentasT = transformar(matVentas)

try:  
    fd = open('ventas.txt', 'w')
    for fila in matVentasT:
        fd.write(fila + '\n') 
         
    fd.close()    
except FileNotFoundError:  
    fd = open('ventas.txt', 'w')
    for fila in matVentasT:
        fd.write(fila + '\n')       
    fd.close()