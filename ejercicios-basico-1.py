"""
1- Definir una funcion max() que tome como argumento dos numeros y devuelva el mayor de ellos.
(Es cierto que python tiene una funcion max() incorporada, pero hacerla nosotros mismos es un muy buen ejercicio).
"""

def funcion_max(n1, n2):
    if n1 > n2:
        return n1
    else:
        return n2

print("Ejercicio 1: ", funcion_max(1,5))

"""
2- Definir una funcion max_de_tres(), que tome tres numeros como argumentos y devuelva el mayor de ellos.
"""

def funcion_max_de_tres(n1,n2,n3):
    if n1 > n2 and n1 > n3:
        return n1
    elif n2 > n3 and n2 > n3:
        return n2
    else:
        return n3

print("Ejercicio 2: ", funcion_max_de_tres(10,-1,2))

"""
3- leer un caracter y verificar si es una vocal
"""

def is_vocal(caracter):
    lista_vocales = ['a','e','i','o','u']
    if caracter in lista_vocales:
        return True
    else:
        return False

print("Ejercicio 3: ", is_vocal('a'))

"""
Escribir una funcion sum() y una funcion multip() que sumen y multipliquen respectivamente todos los numeros de una
lista. por ejemplo: sum([1,2,3,4]) deberia devolver 10 y multip([1,2,3,4]) deberia devolver 24.
"""

def suma(lista):
    resultado = 0
    for n in lista:
        resultado = resultado + (n)

    print("Ejercicio 4: ", resultado)

suma([1,2,3])

def multip(lista):
    resultado = 1
    for n in lista:
        resultado = resultado * (n)

    print("Ejercicio 5: ", resultado)


multip([1,2,3,4])
