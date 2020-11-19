# JOSE ALFREDO ROMERO GONZALEZ 
# 18/11/2020
num = int(input("Ingrese un numero: \n"))
for i in range(num):
    print("*"*(i+1))
    
# SOLUCION 1 DE https://aprendeconalf.es/
n = int(input("Introduce la altura del triángulo (entero positivo): "))
for i in range(n):
    for j in range(i+1):
        print("*", end="")
    print("")
    
# SOLUCION 2 DE https://aprendeconalf.es/
n = int(input("Introduce la altura del triángulo (entero positivo): "))
for i in range(n):
   print("*"*(i+1))
