# JOSE ALFREDO ROMERO GONZALEZ 
# 08/10/2020
n1 = int(input("Ingresa un numero: \n"))
n2 = int(input("Ingresa otro numero: \n"))

c = n1 // n2
r = n1 % n2

print(str(n1) + " entre " + str(n2) + " da un cociente " + str(c) + " y un resto " + str(r))

# SOLUCION  DE https://aprendeconalf.es/
n = input("Introduce el dividendo (entero): ")
m = input("Introduce el divisor (entero): ")
print(n + " entre " +  m + " da un cociente " + str(int(n) // int(m)) + " y un resto " + str(int(n) % int(m)))
