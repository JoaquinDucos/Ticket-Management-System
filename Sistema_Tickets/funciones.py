
def matrizNula ():

    matriz = [None]* 50

    for i in range(len(matriz)):

        matriz[i]= [None] * 50

    return matriz    

def matrizNulaVentas():

    matriz = ['']* 50

    for i in range(len(matriz)):

        matriz[i]= [''] * 50

    return matriz  

def bienvenida():
    print('\n')
    print('*'*54)
    print("*" + ' '*52 +'*')
    print("*      BIENVENID@ AL SISTEMA DE VENTA DE TICKETS" + ' '*5 + '*')
    print("*" + ' '*52 +'*')
    print('*'*54 +'\n')

def llenarMatriz(matriz):

    for i in range(len(matriz)):
        for j in range(len(matriz[0])):
            matriz[i][j] = int(0)

    return matriz        

def sumaMatriz (matriz):

    suma = 0

    for i in range(len(matriz)):
        for j in range(len(matriz[0])):
            suma += matriz[i][j]

    return suma

def printMatriz(matriz):

    k = 0
    l =0
    print("Columna\t", end="")

    for n in range(len(matriz[0])):
        print("\t[", l,"]", end="")
        l +=1

    print("\n")

    for i in range(len(matriz)):
        print("Fila[", k,"]", end="")
        k +=1
        for j in range (len(matriz[0])): 
            print("\t",matriz[i][j], end="   ")    
        print()

def transformar(matriz):
    matriz_nuev= []

    for fila in matriz:
        cadena = ''
        for elemento in fila:
            cadena += str(elemento)+' '
        matriz_nuev.append(cadena)  

    return matriz_nuev                

def asientosLibres(matriz, fila, columna):

    if int(matriz[fila][columna]) == 0:
        return True
    else:
        return False    

def vip(fila): 

    if fila <= 24:
        return True
    else:
        return False

def fullVip(matriz):

    sobra = 0
    cont = 0
    cont2 = 0
    if len(matriz) <= 25:
        for i in range(len(matriz)):
            for j in range(len(matriz[0])):
                if matriz[i][j] == 0 or matriz[j][i] == 0:
                    sobra += 1    

                    if matriz[i][j]== 0:
                        cont +=1
                    if matriz[j][i] == 0:
                        cont2 +=1 
    else:
        for i in range(25):
            for j in range(25):
                if matriz[i][j] == 0 or matriz[j][i] == 0:
                    sobra += 1  

                    if matriz[i][j]== 0:
                        cont +=1
                    if matriz[j][i] == 0:
                        cont2 +=1                  
    if sobra > 0:

        if cont > cont2:
            print(cont2, end="")

        else:
            print(cont2, end="")
        return True 

    else:
        return False                               

def fullAsientos (matriz):

    sobra = 0
    for i in range(len(matriz)):
        for j in range(len(matriz[0])-1):
            if int(matriz[i][j]) == 0 or int(matriz[j][i]) == 0:
                sobra +=1
                
    if sobra == 0:
        return True   
    else:
        return False         

def minuscula(s):
    i = 0
    palabra=''

    while i <len(s):

        if ( ( s[i] > chr(64) and s[i] < chr(91) ) or( s[i] >= '') and s[i] < chr(122) ):

            if s[i] > chr(64) and s[i] < chr(91):
                k = int(ord(s[i]))
                k = k+32
                m = chr(k)
                palabra = str(palabra) + m    

            else:    
                palabra += s[i]
        i +=1     

    return palabra

def es_numero(c):

    c = str(c)
    for letra in c:
        if ( letra < chr(48) or letra > chr(57) ):
            return False
    
    return True    

def usuario_valido(usuario):

    cont = 0
    if (len(usuario) >= 5):

        for i in usuario:
            if es_numero(i) == True:
                cont +=1

            if i == ' ':
                print("\nNombre de usuario contiene espacios\n")
                return False 

        if ( (len(usuario) - cont ) >=5 ):  
            return True

        else:
            print("\nUsuario no contiene 5, o más de 5 letras.\n")
            return False     

    else:
        print("\nNombre de usuario debe contener al menos 5 letras\n")
        return False             

def split(S, c):

    lista=[]
    sub=""

    for i in S:
        if i != c:
            sub += i  
        else:
            lista.append(sub)
            sub = ""    

    if sub != "":
        lista.append(sub) 
            
    return lista

def strip(S):
    txt =''
    i, cont1, cont2 = 0, 0, 0
    inverso = S[::-1]

    try:
        while S[i] == ' ':
            cont1 += 1
            i +=1   

        i = 0      

        while inverso[i] == ' ':
            cont2 += 1
            i +=1          

        txt = S[cont1:len(S)-(cont2):1]

    except IndexError:
        print("Error")    

    return txt      

def num_ticket (num):

    num = str(num)
    n = ''

    if len(num) < 4:
        n += '0'*(4-len(num))
    n = n + num  

    return n  

def buscar_subcadena (S, sub):

    for i in S:
        if sub in S:
            return True
            
def transformar_archivo (archivo):
    try:    
        archivo = open (archivo, "r")
        matriz = split (archivo.read(), "\n") 
        matriz_aux= []
        cont = 0
        
        for fila in matriz:
            fila = split(fila, " ")
            matriz_aux.append(fila) 
            #Eliminamos el print de las filas.
            if matriz[cont][0] != '0' or  matriz_aux[cont][0] != '1':
                del matriz_aux[cont][0]
                cont += 1
    
        #Elimina la primer fila que contiene únicamente el print de columnas.
        del matriz_aux[0]
        return matriz_aux

    except FileNotFoundError:

        print("No existe el archivo 'asientos.txt', crearemos uno nuevo\n")  
        mNula = matrizNula()
        matrizAsientos = llenarMatriz(mNula)     

        return matrizAsientos 

def transformar_archivo_ventas(archivo):
    try:    
        archivo = open (archivo, "r")
        matriz = split (archivo.read(), "\n") 
        matriz_aux= []

        for fila in matriz:
            fila = split (fila, " ")
            matriz_aux.append(fila) 
        archivo.close ()  

        return matriz_aux

    except FileNotFoundError:
        print("No existe el archivo 'ventas.txt', crearemos uno nuevo\n")  
        matrizAsientos = []

        return matrizAsientos            

def menu():
    print('\n')
    print('*'*54)
    print("*" + ' '*52 +'*')
    print("*" + ' '*15 +'| MUSIC FESTIVAL 2023 |'+' '*14 +'*')
    print("*" + ' '*5 + 'MENU:' + ' '*42 + '*') 
    print("*" + ' '*52 + '*\n'
        "*     1.  Mostrar asientos disponibles               *\n" 
        "*     2.  Realizar compra                            *\n" 
        "*     3.  Generar Ticket                             *\n"
        "*     4.  Registrar venta                            *\n"
        "*     5.  Buscar asiento por usuario                 *\n"
        "*     6.  Usuarios VIP ordenados (A a Z)             *\n"
        "*     7.  Mostrar edades promedio por sector         *\n" 
        "*     8.  Pérdida de Ticket                          *\n"
        "*     9.  Recaudación Total                          *\n"
        "*     10. Compradores menores de 21 años             *\n"
        "*     11. Salir                                      *")
    print("*" + ' '*52 + '*')   
    print("*"*54 +'\n')
    n=None

    while n==None:

        try :

            n=input("\nSeleccione el tipo de operación que desea realizar: ")
            n=int(n)

            while n > 11 or n < 1:

                print("\nAcción Inválida\n")
                n= int(input("\nIntente nuevamente: "))

                while not es_numero(n):

                    print("\nAcción Inválida")
                    n= int(input("\nIntente nuevamente: "))
            print('\n')
        except TypeError and ValueError: 
            print("\nLas operaciones estan designadas por números.\n\n")
            n = None

    return n    

def matrizSobreMarcha(mat, cont, usuario, dni, edad, monto, f, c):

        for i in range(cont-1, cont):
            lista=[]
            for j in range(1):
                lista_str = ( usuario +' '+ dni +' '+ edad +' '+ monto +' '+ " F{" + str(f) + "}C{"+ str(c) + "}")
                lista_str = split(lista_str, " ")
                lista = lista_str
            mat.append(lista)    

        return mat

def pedirAsiento(f, c):  
            
    #VERIFICO QUE NO ESTÉN FUERA DE RANGO LAS FILAS Y COLUMNAS (Rango de la matriz seleccionada anteriormente).       
    while( f >= 50 or c >= 50):  
        print("\nIngrese fila y columna (separados por ':') para comprar el asiento. Únicamente valores dentro del rango y sin caracteres de más por favor.\n")     
        f = str(f)
        c = str(c)
        try:                                #Pedir fila y columna en la misma línea, con un formato como fila : columna.
                f, c = input().split(":")
                f, c = strip(f),strip(c)
                f, c = int(f), int(c)

        except ValueError or IndexError:    
                print("Has introducido un caracter inválido.")
                f = 50
                c= 50 

        while ( not es_numero(f) ) or (not es_numero(c)):             #VERIFICO QUE SEAN NÚMEROS ÚNICAMENTE. 
            print("Ingrese números únicamente.(Sin caracteres de más)\n") 

            try: 

                f, c = input().split(":")

            except ValueError or IndexError:
                print("Has introducido un caracter inválido.")
                f = 50
                c= 50 
    return f, c    

def cont_ticket(matriz):

    cont = 0

    for i in range(len(matriz)):
        for j in range(len(matriz[1])):
            if int(matriz[i][j]) == 1:
                cont += 1
    return cont            

def datos_compra():

    print("Vamos a pedirle unos datos para su compra:\n")
    dni = ''
    edad = 0
    
    #Verifico que el dni sea un número y con 7 u 8 dígitos únicamente.
    print("\nIngrese nombre de usuario. Debe contener al menos 5 letras!")    
    usuario = input("Usuario: ")

    while not usuario_valido(usuario):
        print("Ingrese nuevamente.")
        usuario = input("Usuario: ") 

    while (edad < 10 or edad > 110):
        edad = str(edad)
        edad = input("Ingrese un rango de edad válido entre 10 y 110 años: ") 

        while not es_numero(edad):
            print("Ingrese únicamente números.")
            edad = input("Edad: ")
        edad = int(edad)
    edad = str(edad) 

    while (not es_numero(dni)) or (len(dni) < 7 or len(dni) > 8):
        print("ingrese únicamente números de 7 u 8 dígitos.")
        dni = input("DNI: ")  

    return usuario,dni,edad      

def buscarUsuarios(usuario, matVentas):
    cont = 0
    num = 0

    try:

        for fila in matVentas:
          num += 1  
          for columna in fila:
            
            if columna == usuario:

                col = num
                cont +=1
                f = matVentas[col-1][3]
                c= matVentas[col-1][4]
                print("\nEl usuario ocupó el/los Asiento/s f{", f,'} c{', c, '}' )

        if cont < 1:      
            print("\nEl usuario no ha sido registrado previamente. Usted no tiene un asiento asignado")  
        
    except IndexError:
        print("\nERROR: No se ha registrado ninguna compra aún\n")

def usuario_vip_alfabet(matVentas):

    lista_usuarios =[]
    try:

        for fila in matVentas:
            if int(fila[3]) < 25:
                lista_usuarios.append(fila[0])   

        return lista_usuarios

    except IndexError:    
        print("\nNo se ha realizado una compra en el sector VIP aún.\n")

def cont_filas_ventas(matVentas):
    num = 0
    for fila in matVentas:
        num += 1   

    return num           

def list_to_str (lista):

    string = ''
    for elemento in lista:
        
        string += str(elemento) + ' '

    return string 

def list_to_str_comas (lista):

    string = ''
    for elemento in lista:
        if elemento != lista[len(lista)-1]:
            string += str(elemento) + ', '
        else:     
            string += str(elemento) + '.'

    return string 

def burbujeo(lista):

    for i in range(len(lista)-1):
        for j in range(i + 1, len(lista)):

            if minuscula(lista[i]) > minuscula(lista[j]):
                aux = lista[i]
                lista[i]=lista[j]
                lista[j] = aux

    return lista

def buscar_ticket(num):

  num = num_ticket(num)

  try:

    fd = open('ticket_' + num + '.txt', 'r')
    print("\nBuscando ticket en base de datos . . . \n\nSe encontró 1 ticket.\n\n\n\t -----------\n")
    for i in fd:
      print(i)
    print("\n", end='')
    fd.close()
    print("\t -----------")

  except FileNotFoundError:
    print("Su numero de ticket no existe:(\nRecordatorio: Debe ser un número y no mayor a 4 cifras!\n\nSi desea, proceda a comprar una entrada!\n")    

def salida():

    pregunta = input("\n¿Seguro que desea Salir? ( Si/No ): ")
    pregunta = minuscula(pregunta)   

    while( pregunta != 'si' and pregunta != 'no'):
        pregunta = input("\nIntroduce una respuesta válida ( Si/No ): ")
        pregunta = minuscula(pregunta)

    if pregunta == 'si':  

        print("\nGuardando información en la base de datos . . .\n\nGuardado!\n\nGracias por usar nuestro sistema. Hasta pronto!\n")   
        return True

    else:
        return False   

def imprimir_venta(lista_usr, matVentas):
    
    print("\n\t\tUsuarios ordenados con sus respectivas compras: \n")
    for usuario in lista_usr:
        for fila in matVentas:
            if fila[0] == usuario:

                fila_datos = ("Usuario: ", fila[0],"\t DNI:", fila[1], "\tEdad:",  fila[2], "\tAsiento: F{" + str(fila[3]) + "}\tC{" + str(fila[4]) +"}")
                fila_datos = list_to_str(fila_datos)

        print(fila_datos)   

def promedio_edad (matVentas):

  contV, contG, edadVip, edadGral, contFila = 0, 0, 0, 0, 0 

  for fila in matVentas:
    for columna in fila:

        if int(fila[3]) < 25:
            contV+=1
            edadVip+=int(matVentas[contFila][2])

        elif int(fila[3]) > 24:
            contG+=1
            edadGral+=int(matVentas[contFila][2])
       
    contFila +=1

  try:  
    promedioGral = round((edadGral/contG),3)
    

  except ZeroDivisionError:

    print("\nNo se ha registrado ninguna venta en el sector General\n")  
    promedioGral = 0
  try:  
    promedioVip = round((edadVip/contV), 3)

  except ZeroDivisionError:

    print("\nNo se ha registrado ninguna venta en el sector VIP\n")  
    promedioVip= 0

  return promedioGral, promedioVip

def recaudacion (matVentas):

  montoTot=0
  MONTO_VIP = 20000
  MONTO_GRAL = 15000

  for fila in matVentas:

    if int(fila[3]) < 25:

        montoTot += MONTO_VIP
    else:
        montoTot += MONTO_GRAL

  return montoTot 

def usuarios_u21(matventas):

    lista_u21=[]
    try:
    
        for fila in matventas:
            if int(fila[2]) <= 21:
                lista_u21.append(fila[0])
        
        return lista_u21

    except IndexError:
        print()
