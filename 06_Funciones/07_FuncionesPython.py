# JOSE ALFREDO ROMERO GONZALEZ 
# 26/11/2020
def cuadrados(l_n):
    l_n2 = []
    for n in l_n:
        l_n2.append(n**2)
    return l_n2

l_n = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print("Lista con original:", l_n)
print("Lista con sus numeros al cuadrado:", cuadrados(l_n))


# SOLUCION 1 DE https://aprendeconalf.es/
def square(sample):
    """Función que calcula los cuadrados de una lista de números.
    Parámetros
    sample: Es una lista de números
    Devuelve una lista con los cuadrados de los números de la lista sample.
    """
    list = []
    for i in sample:
        list.append(i**2)
    return list

print(square([1, 2, 3, 4, 5]))
print(square([2.3, 5.7, 6.8, 9.7, 12.1, 15.6]))

# SOLUCION 2 DE https://aprendeconalf.es/
def square(*sample):
    """Función que calcula los cuadrados de una lista de números.
    Parámetros
    *sample: Es una secuencia de números separados por comas.
    Devuelve una lista con los cuadrados de los números de sample.
    """
    list = []
    for i in sample:
        list.append(i**2)
    return list

print(square(1, 2, 3, 4, 5))
print(square(2.3, 5.7, 6.8, 9.7, 12.1, 15.6))
