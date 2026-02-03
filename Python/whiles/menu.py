'''opcion = int(input("Elija la opción: 1.-ver menú. 2.-Pedir de comer. 3.-Salir. "))

while opcion != 3: 
    if opcion == 1:
        print("-Chorizo. -tarta. -bebida")
        break
    elif opcion == 2:
        print("qué va a pedir?: -Chorizo. -tarta. -bebida")
        break
    elif opcion == 3:
        print("Gracias por visitar")
#ESTE ES MI CODIGO, EL QUE HICE SIN VER PISTAS, Y ESTÁ "MAL" PORQUE NO SE REPITE
'''
'''
opcion = 0

while opcion != 3: 
    print("1. Saludar")
    print("2. Mostrar mensaje")
    print("3. Salir")

    opcion = int(input("Elige una opción: "))

    if opcion == 1:
        print("Hola. Bienvenido!")
    elif opcion == 2:
        print("Este es un mensaje secreto")
    else:
        print("ADIOS!")
'''

opcion = 0

while opcion != 3:
    opcion = int(input("1.-Ver menú  2.-Pedir de comer  3.-Salir: "))

    if opcion == 1:
        print("- Chorizo")
        print("- Tarta")
        print("- Bebida")

    elif opcion == 2:
        print("¿Qué va a pedir?")

    elif opcion == 3:
        print("Gracias por visitar")
#versión mía corregida x chatgpt