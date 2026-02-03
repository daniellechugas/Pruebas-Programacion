opcion = 0 
saldo = 100

while opcion != 4:
    print("//1. Ver saldo. //2. Depositar. //3. Retirar. //4. Salir. ")
    opcion = int(input("OPCION: #"))

    if opcion == 1: 
        print("Tienes: $", saldo)

    elif opcion ==  2:
        saldo = saldo + int(input("¿Cuanto deseas depositar?: $")) #lo propuso chatgpt ( antes solo: saldo = int(input("¿Cuanto deseas depositar?: $")) )

    elif opcion == 3:
        print(f"¿Cuanto deseas retirar?. Tienes ${saldo}: ")
        retiro = int(input("RETIRAR: $"))   #tuve problemas con esta linea, estaba poniendo saldo en vez retiro
        
        if retiro > saldo:
            print("No tienes suficiente saldo")            
            
        else:
            saldo = saldo - retiro
            print(f"Retiro exitoso. Tu nuevo saldo es: ${saldo}")

    else:
        print("Gracias. ¡Buen día!.")

