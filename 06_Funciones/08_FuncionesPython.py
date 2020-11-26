# JOSE ALFREDO ROMERO GONZALEZ 
# 26/11/2020
def estadistica(l_n):
    d_est = {}
    d_est['Media'] = sum(l_n)/len(l_n)
    var = 0
    for n in l_n:
        var += (n-d_est['Media'])**2
    d_est['Varianza'] = var/len(l_n)
    d_est['Desviacion estandar'] = d_est['Varianza'] ** (1/2)

    return d_est

l_n = [2.3, 5.7, 6.8, 9.7, 12.1, 15.6]
d_est = estadistica(l_n)
for k, v in d_est.items():
    print(k, ":", v)

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

def statistics(sample):
    """Función que calcula la media, varianza y desviación típica de una muestra de números.
    Parámetros
    sample: Es una lista de números
    Devuelve un diccionario con la media, varianza y desviación típica de los números en sample.
    """
    stat = {}
    stat['media'] = sum(sample)/len(sample)
    stat['varianza'] = sum(square(sample))/len(sample)-stat['media']**2
    stat['desviacion tipica'] = stat['varianza']**0.5
    return stat

print(statistics([1, 2, 3, 4, 5]))
print(statistics([2.3, 5.7, 6.8, 9.7, 12.1, 15.6]))

# SOLUCION 2 DE https://aprendeconalf.es/
def square(*sample):
    """Función que calcula los cuadrados de una lista de números.
    Parámetros
    sample: Es una secuencia de números separados por comas.
    Devuelve una lista con los cuadrados de los números de sample.
    """
    list = []
    for i in sample:
        list.append(i**2)
    return list

def statistics(*sample):
    """Función que calcula la media, varianza y desviación típica de una muestra de números.
    Parámetros
    sample: Es una secuencia de números separados por comas.
    Devuelve un diccionario con la media, varianza y desviación típica de los números en sample.
    """
    stat = {}
    stat['media'] = sum(sample)/len(sample)
    stat['varianza'] = sum(square(*sample))/len(sample)-stat['media']**2
    stat['desviacion tipica'] = stat['varianza']**0.5
    return stat

print(statistics(1, 2, 3, 4, 5))
print(statistics(2.3, 5.7, 6.8, 9.7, 12.1, 15.6))
