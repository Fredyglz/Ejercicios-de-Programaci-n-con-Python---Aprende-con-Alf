# JOSE ALFREDO ROMERO GONZALEZ 
# 26/11/2020
def media(l_n):
    return sum(l_n)/len(l_n)

l_n = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print("Media:", media(l_n))

# SOLUCION 1 DE https://aprendeconalf.es/
def mean(sample):
    """Función que calcula la media de una muestra de números.
    Parámetros
    sample: Es una lista de números
    Devuelve la media de los números en sample. 
    """
    return sum(sample)/len(sample)

print(mean([1, 2, 3, 4, 5]))
print(mean([2.3, 5.7, 6.8, 9.7, 12.1, 15.6]))

# SOLUCION 2 DE https://aprendeconalf.es/
def mean(*sample):
    """Función que calcula la media de una muestra de números.
    Parámetros
    *sample: Secuencia de números separados por comas.
    Devuelve la media de los números en *sample. 
    """
    return sum(sample)/len(sample)

print(mean(1, 2, 3, 4, 5))
print(mean(2.3, 5.7, 6.8, 9.7, 12.1, 15.6))
