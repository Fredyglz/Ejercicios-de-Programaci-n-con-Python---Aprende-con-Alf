# JOSE ALFREDO ROMERO GONZALEZ 
# 26/11/2020
def mcdFuncion(n1, n2):
    minimo = min(n1, n2) 
    for d in range(2, minimo+1):
        if (n1 % d == 0) and (n2 % d == 0):
            mcd = d
    return mcd

def mcmFuncion(n1,n2):
    mcm1 = n1
    mcm2 = n2
    while True:
        if mcm1 <= mcm2:
            if mcm1 != mcm2:
               mcm1 += n1 
            else:
                return mcm1
        else:
            mcm2 += n2

print("Máximo común divisor:", mcdFuncion(24,36))
print("Minimo común multiplo:", mcmFuncion(24,36))

# SOLUCION DE https://aprendeconalf.es/
def mcd(n, m):
    """Función que calcula el máximo común divisor de dos números.
    Parámetros:
        - n: Es un número entero.
        - m: Es un número entero.
    Devuelve:
        El máximo común divisor de n y m.
    """
    rest = 0
    while(m > 0):
        rest = m
        m = n % m
        n = rest
    return n

def mcm(n, m):
    """Función que calcula el mínimo común múltiplo de dos números.
    Parámetros:
        - n: Es un número entero.
        - m: Es un número entero.
    Devuelve:
        El mínimo común múltiplo de n y m.
    """
    if n > m:
        greater = n
    else:
        greater = m
    while (greater % n != 0) or (greater % m != 0):
        greater += 1
    return greater

print(mcd(24,36))
print(mcm(24,36))
