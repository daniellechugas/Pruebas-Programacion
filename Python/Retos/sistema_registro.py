''' usuarios = []

while len(usuarios) < 3:
    
    usuario = input("Usuario: ")

    if usuario == "":
        print("no puede estar vacío.")
        continue
    
    if not usuario.isalnum():
        print("Solo letras y números.")
        continue
    
    if usuario in usuarios:
        print("Ya existe ese usuario.") 
        continue

    nombre = input("Nombre real: ")

    if nombre == "":
        print("Nombre vacío")
        continue

    if not nombre.replace(" ", "").isalpha():
        print("Solo letras en el nombre.")
    
    usuarios.append(usuario)
    print("Usuarios registrados correctamente.")

print("Usuarios finales:", usuarios)


'''

usuarios = []

while len(usuarios) < 3:

    usuario = input("Usuario: ")

    if usuario == "":
        print("No puede estar vacío")
        continue

    if not usuario.isalnum():
        print("Solo letras y números")
        continue

    if usuario in usuarios:
        print("Ese usuario ya existe")
        continue

    nombre = input("Nombre real: ")

    if nombre == "":
        print("Nombre vacío")
        continue

    if not nombre.replace(" ", "").isalpha():
        print("Solo letras en el nombre")
        continue

    usuarios.append(usuario)
    print("Usuario registrado correctamente")

print("Usuarios finales:", usuarios)
