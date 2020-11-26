# JOSE ALFREDO ROMERO GONZALEZ 
# 26/11/2020
def factorial(n):
    if n < 2:
        return 1
    return n * factorial(n-1)

n = 20
fac = factorial(n)
print("El factorial de " + str(n) + " es " + str(fac))

# SOLUCION DE https://aprendeconalf.es/
def factorial(n):
    """Función que calcula el factorial de un número entero positivo.
    Parámetros
    n: Es un entero positivo.
    Devuelve el factorial de n.
    """
    tmp = 1
    for i in range(n):
        tmp *= i+1
    return tmp

print(factorial(4))
print(factorial(20))
