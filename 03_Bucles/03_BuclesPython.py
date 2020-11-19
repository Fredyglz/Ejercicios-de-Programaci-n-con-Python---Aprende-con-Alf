# JOSE ALFREDO ROMERO GONZALEZ 
# 18/11/2020
num = int(input("Ingrese un numero entero positivo: \n"))
for i in range(1,num+1):
    if i % 2 != 0:
        print(i, end=", ")
    
# SOLUCION DE https://aprendeconalf.es/
n = int(input("Introduce un número entero positivo: "))
for i in range(1, n+1, 2):
    print(i, end=", ")
