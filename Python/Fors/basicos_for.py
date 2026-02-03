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
'''
for i in range(1, 11):
    if i % 2 != 0:
        print(i)
    
    
