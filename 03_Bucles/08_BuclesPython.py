# JOSE ALFREDO ROMERO GONZALEZ 
# 18/11/2020
n = int(input("Ingrese un numero: \n"))
for i in range(1, n+1, 2):
    for j in range(i, 0, -2):
        print(j,end=" ")
    print("\n")
    
# SOLUCION DE https://aprendeconalf.es/
n = int(input("Introduce la altura del triángulo (entero positivo): "))
for i in range(1, n+1, 2):
    for j in range(i, 0, -2):
        print(j, end=" ")
    print("")
