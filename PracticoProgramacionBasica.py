import os
clear = lambda: os.system('cls')

def Pantalla1():
    clear()
    active = False
    while not active:
        try:
            sexo = input('Introduzca el sexo con el cual se identifica (F) o (M)\n')
            
            if sexo == "F" or sexo == "M":
                retorno =  True
            else:
                retorno = False
            print("El sexo seleccionado es", sexo, "Su retorno es", retorno)
            opcion = input('Desea continuar: S/N\n')
            if(opcion == 'N' or opcion == 'n'):
                active = True
        except:
            print('Por favor introduzca un valor F o M')
        
def Pantalla2():
    clear()
    active = False
    while not active:
        try:
            age = int(input('Introduzca su edad\n'))
            
            if age > 18:
                retorno =  True
            else:
                retorno = False
            print("Su edad es", age, "Su retorno es", retorno)
            opcion = input('Desea continuar: S/N\n')
            if(opcion == 'N' or opcion == 'n'):
                active = True
        except:
            print('Por favor introduzca un valor numerico')
        
def Pantalla3():
    clear()
    active = False
    while not active:
        try:
            age = int(input('Introduzca su edad\n'))
            
            if age < 10 or age >60:
                retorno =  True
            else:
                retorno = False
            print("Su edad es", age, "Su retorno es", retorno)
            opcion = input('Desea continuar: S/N\n')
            if(opcion == 'N' or opcion == 'n'):
                active = True
        except:
            print('Por favor introduzca un valor numerico')

def Pantalla4():
    clear()
    active = False
    while not active:
        try:
            grados = int(input('Introduzca su grados Fahrenheit\n'))
            
            celsius = (grados - 32)/1.8000
            print("Sus grados en F son", grados, "Sus grados en Celsius son", celsius)
            opcion = input('Desea continuar: S/N\n')
            if(opcion == 'N' or opcion == 'n'):
                active = True
        except:
            print('Por favor introduzca un valor numerico')
        

def Pantalla5():
    clear()
    active = False
    while not active:
        try:
            n1 = int(input('Introduzca su un número\n'))
            n2 = int(input('Introduzca su un número\n'))
            n3 = int(input('Introduzca su un número\n'))
            n4 = int(input('Introduzca su un número\n'))
            n5 = int(input('Introduzca su un número\n'))
            
            arrayNums = []
            arrayNums.append(n1)
            arrayNums.append(n2)
            arrayNums.append(n3)
            arrayNums.append(n4)
            arrayNums.append(n5)
            if arrayNums[2]%2 == 0 and arrayNums[3]%2 == 0 and arrayNums[4]%2 == 0:
                retorno =  True
            else:
                retorno = False
            print(retorno)
            opcion = input('Desea continuar: S/N\n')
            if(opcion == 'N' or opcion == 'n'):
                active = True
        except:
            print('Por favor introduzca un valor numerico')

def Pantalla6():
    clear()
    active = False
    while not active:
        try:
            n1 = int(input('Introduzca su un número\n'))
            n2 = int(input('Introduzca su un número\n'))
            n3 = int(input('Introduzca su un número\n'))
            n4 = int(input('Introduzca su un número\n'))
            n5 = int(input('Introduzca su un número\n'))
            
            arrayNums = []
            arrayNums.append(n1)
            arrayNums.append(n2)
            arrayNums.append(n3)
            arrayNums.append(n4)
            arrayNums.append(n5)
            cont = 0
            for num in arrayNums:
                if num%2 == 0:
                    cont = cont + 1
            
            if cont >= 1:
                retorno =  True
            else:
                retorno = False     
            print(retorno)
            opcion = input('Desea continuar: S/N\n')
            if(opcion == 'N' or opcion == 'n'):
                active = True
        except:
            print('Por favor introduzca un valor numerico')


def Pantalla7():
    clear()
    active = False
    while not active:
        try:
            p1 = input('Introduzca una palabra\n')
            p2 = input('Introduzca una palabra\n')

            if p1 == p2:
                retorno =  True
            else:
                retorno = False     
            print(retorno)
            opcion = input('Desea continuar: S/N\n')
            if(opcion == 'N' or opcion == 'n'):
                active = True
        except:
            print('Por favor introduzca un valor numerico')

def Pantalla8():
    clear()
    active = False
    while not active:
        try:
            dia = int(input('Ingrese un día de la semana (valor númerico en el que 1 es Lunes y 7 es Domingo)\n'))
            if int(dia) == 1:
                print("Lunes")
            elif int(dia) == 2:
                print("Martes")
            elif int(dia) == 3:
                print("Miercoles")
            elif int(dia) == 4:
                print("Jueves")
            elif int(dia) == 5:
                print("Viernes")
            elif int(dia) == 6:
                print("Sabado")
            elif int(dia) == 7:
                print("Domingo")
            else:
                print("Usted no ingreso un valor correcto") 
            opcion = input('Desea continuar: S/N\n')
            if(opcion == 'N' or opcion == 'n'):
                active = True
        except:
            print('Por favor introduzca un valor numerico')

def Pantalla9():
    clear()
    active = False
    while not active:
        try:
            numero = input('Ingrese un numero\n')
            if numero == numero[::-1]:
                 retorno =  True
            else:
                retorno = False     
            print(retorno)
            opcion = input('Desea continuar: S/N\n')
            if(opcion == 'N' or opcion == 'n'):
                active = True
        except:
            print('Por favor introduzca un valor numerico')

def Pantalla10():
    clear()
    active = False
    while not active:
        try:
            numero = int(input('Ingrese un numero\n'))
            numeroB = int(input('Ingrese un numero\n'))
            if numero <numeroB:
                 retorno =  True
            else:
                retorno = False     
            print(retorno)
            opcion = input('Desea continuar: S/N\n')
            if(opcion == 'N' or opcion == 'n'):
                active = True
        except:
            print('Por favor introduzca un valor numerico')

def Pantalla11():
    clear()
    active = False
    while not active:
        try:
            numero = int(input('Ingrese un numero\n'))
            numeroB = int(input('Ingrese un numero\n'))
            if numero *numeroB == numero/numeroB:
                 retorno =  True
            else:
                retorno = False     
            print(retorno)
            opcion = input('Desea continuar: S/N\n')
            if(opcion == 'N' or opcion == 'n'):
                active = True
        except:
            print('Por favor introduzca un valor numerico')

def Pantalla12():
    clear()
    active = False
    while not active:
        try:
            n1 = int(input('Introduzca su un número\n'))
            n2 = int(input('Introduzca su un número\n'))
            n3 = int(input('Introduzca su un número\n'))
            n4 = int(input('Introduzca su un número\n'))
            n5 = int(input('Introduzca su un número\n'))
            m1 = int(input('Introduzca su un número\n'))
            m2 = int(input('Introduzca su un número\n'))
            m3 = int(input('Introduzca su un número\n'))
            m4 = int(input('Introduzca su un número\n'))
            m5 = int(input('Introduzca su un número\n'))
            
            arrayNums = []
            arrayNumsB = []
            arrayNums.append(n1)
            arrayNums.append(n2)
            arrayNums.append(n3)
            arrayNums.append(n4)
            arrayNums.append(n5)
            arrayNumsB.append(m1)
            arrayNumsB.append(m2)
            arrayNumsB.append(m3)
            arrayNumsB.append(m4)
            arrayNumsB.append(m5)
            cont = 0
            for i in arrayNums:
                if i in arrayNumsB:
                    cont += 1
            if cont >= 1:
                retorno=  True
            else:
                retorno= False 
            print(retorno)
            opcion = input('Desea continuar: S/N\n')
            if(opcion == 'N' or opcion == 'n'):
                active = True
        except:
            print('Por favor introduzca un valor numerico')


def Pantalla13():
    clear()
    active = False
    while not active:
        try:
            palabra = input('Ingrese una palabra\n')
            print(palabra[::-1])
            opcion = input('Desea continuar: S/N\n')
            if(opcion == 'N' or opcion == 'n'):
                active = True
        except:
            print('Por favor introduzca un valor numerico')

def Pantalla14():
    clear()
    active = False
    while not active:
        try:
            palabra = input('Ingrese una palabra\n')
            vocales = ["a", "e", "i", "o", "u"]

            for letra in palabra:
                if letra in vocales:
                    palabra = palabra.replace(letra, "x")
                    
            print(palabra)
            opcion = input('Desea continuar: S/N\n')
            if(opcion == 'N' or opcion == 'n'):
                active = True
        except:
            print('Por favor introduzca un valor numerico')



active = False
while not active:
    clear()
    print('Un clasico:')
    print('1 - Elige tu sexo')
    print('2 - Mayor de edad')
    print('3 - Edad < 10 o >60')
    print('4 - Conversor de grados')
    print('5 - posiciones pares en un array')
    print('6 - Mas de un par en un array')
    print('7 - Palabras iguales')
    print('8 - Días de la semana')
    print('9 - Es capicua?')
    print('10 - < o >')
    print('11 - a*b = a/b')
    print('12 - A en B')
    print('13 - Al reves')
    print('14 - Vocales a x')
    print('15 - Exit')
    opcion = input('Introduce un numero:')
    try:
        if int(opcion) == 1:
            Pantalla1()
        elif int(opcion) == 2:
            Pantalla2()
        elif int(opcion) == 3:
            Pantalla3()
        elif int(opcion) == 4:
            Pantalla4()
        elif int(opcion) == 5:
            Pantalla5()
        elif int(opcion) == 6:
            Pantalla6()
        elif int(opcion) == 7:
            Pantalla7()
        elif int(opcion) == 8:
            Pantalla8()
        elif int(opcion) == 9:
            Pantalla9()
        elif int(opcion) == 10:
            Pantalla10()
        elif int(opcion) == 11:
            Pantalla11()
        elif int(opcion) == 12:
            Pantalla12()
        elif int(opcion) == 13:
            Pantalla13()
        elif int(opcion) == 14:
            Pantalla14()
        elif int(opcion) == 15:
            print('Saliendo')
            active = True   
    except:
        print("Por favor introduzca una opcion valida")
    