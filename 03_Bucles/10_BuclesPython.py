# JOSE ALFREDO ROMERO GONZALEZ 
# 18/11/2020
n = int(input("Ingrese un numero positivo entero mayor que 2: \n"))
for i in range(2,n):
    if n % i == 0:
        break
if (i+1) == n:
    print(n, "es un numero primo")
else: 
    print(n, "no es un numero primo")

# SOLUCION 1 DE https://aprendeconalf.es/
n = int(input("Introduce un número entero positivo mayor que 2: "))
i = 2
while n % i != 0:
    i += 1
if i == n:
    print(str(n) + " es primo")
else:
    print(str(n) + " no es primo")
    
# SOLUCION 2 DE https://aprendeconalf.es/
n = int(input("Introduce un número entero positivo mayor que 2: "))
for i in range(2, n):
    if n % i == 0:
        break
if (i + 1)  == n:
    print(str(n) + " es primo")
else: 
    print(str(n) + " no es primo")
