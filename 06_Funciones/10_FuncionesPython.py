# JOSE ALFREDO ROMERO GONZALEZ 
# 26/11/2020
def decToBin(n):
    decimal = ""
    while n > 1:
        decimal = str(int(n%2)) + decimal
        n /= 2
    return decimal

def binToDec(n):
    sum = 0
    stringN = str(n)
    for i in range(len(stringN)-1,-1,-1):
        sum += int(stringN[i])*(2**(len(stringN)-1-i))
    return sum

print("Decimal a binario:", decToBin(28))
print("Binario a decimal:", binToDec(10101100))

# SOLUCION DE https://aprendeconalf.es/
def to_decimal(n):
    """Función que convierte un número binario en decimal.
    Parámetros:
        - n: Es una cadena de ceros y unos.
    Devuelve:
        El número decimal correspondiente a n.
    """
    n = list(n)
    n.reverse()
    decimal = 0
    for i in range(len(n)):
        decimal += int(n[i]) * 2 ** i
    return decimal

def to_binary(n):
    """Función que convierte un número decimal en binario.
    Parámetros:
        - n: Es un número entero.
    Devuelve:
        El número binario correspondiente a n.
    """
    binary = []
    while n > 0:
        binary.append(str(n % 2))
        n //= 2
    binary.reverse()
    return ''.join(binary)

print(to_decimal('10110'))
print(to_binary(22))
print(to_decimal(to_binary(22)))
print(to_binary(to_decimal('10110')))
