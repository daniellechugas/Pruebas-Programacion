#inicial range(inicio, fin, salto)

'''
for i in range(1, 6):
    print(i)


for i in range(2, 11, 2):
    print(i)

#---ACUMULADOR:---
suma =  0

for i in range(1, 6):
    suma = suma + i

print(suma) #debe mostrar 15
#OJO: la operación se tiene que hacer con la variable que se usará como acumulador, sino saldrá solo las veces que cuente el for

#CUENTA REGRESIVA
for i in range(10, -1, -1):
    print(i)

    #Imprime solo los números impares del 1 al 10 usando for.
for i in range(1, 11):
    if i % 2 != 0:
        print(i)
 # también puede ser así, y más fácil:
for i in range(1, 11, 2): 
    print(i)
    '''
#Pide un número al usuario e imprime los números del 1 hasta ese número usando for.
limite = int(input("Dame un límite: "))

for i in range(1, limite):
    print(i + 1) 
