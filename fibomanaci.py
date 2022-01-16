'''
Secuencia de numeros infinita naturales, a partir del 0 y 1 se van sumando a pares, de manera que cada numero
es igual a la suma de sus dos numero anteriores:
ejemplo: 0,1,1,2,3,5,8,13,21,34,55....
'''
cantidad = int(input("Cantidad de la secuencia"))

n1, n2 = 0, 1
contador = 0

if cantidad <= 0:
    print("Agregar un numero positivo")
elif cantidad == 1:
    print(n1)
else:
    while contador < cantidad:
        print(n1)
        nth = n1 + n2
        n1 = n2
        n2 = nth
        contador += 1
