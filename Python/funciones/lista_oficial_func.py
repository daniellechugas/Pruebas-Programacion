lista_oficial = ["Maite", "Dana", "Diana", "Magui"]

# Creamos el "comando" para buscar
def verificar_acceso(nombre_a_revisar, lista):
    if nombre_a_revisar in lista:
        return True # "Regresa" un resultado positivo
    else:
        return False # "Regresa" un resultado negativo

# Ahora el programa principal es súper limpio:
intento = input("¿Quién intenta entrar? ")

if verificar_acceso(intento, lista_oficial):
    print("Acceso concedido")
else:
    print("Acceso denegado")