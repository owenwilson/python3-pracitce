"""
6- Definir una funcion inversa() que calcule la inversion de una cadena. Por ejemplo la cadena (estoy probando) deberia devolverme
la cadena (obnaborp yotse).
"""

def inversa(cadena):
    longitud = -(len(cadena)-1)
    nueva_cadena = str()
    for n in range(longitud,1):
        n = abs(n)
        nueva_cadena += cadena[n]
        
    return nueva_cadena
    #print("Ejercicio 6: ", nueva_cadena)

#inversa('pepito')


"""
7-
"""

def es_palindromo(cadena):
    nueva_cadena = inversa(cadena)
    if nueva_cadena == cadena:
        return True
    else:
        return False

print(es_palindromo('futbool'))

"""
8-
"""

def superposicion(lista1,lista2):
    for elem in lista1:
        if elem in lista2:
            return True

    return False


print("superposicion:", superposicion([1,2,3],[4,4,5]))

"""
9-
"""

def generar_n_caracteres(caracter,n):
    print(caracter * n)
    """
    string = caracter
    for i in range(1,n):
        string += caracter

    print(string)
    """

generar_n_caracteres('x',5)

"""
10-
"""

def procedimiento(lista):
    for n in lista:
        histograma = '*' * n
        print(f'{histograma} \n')

procedimiento([5,2,7])
