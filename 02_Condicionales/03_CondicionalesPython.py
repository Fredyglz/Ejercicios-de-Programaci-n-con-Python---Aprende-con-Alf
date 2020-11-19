# JOSE ALFREDO ROMERO GONZALEZ 
# 12/10/2020
num1 = float(input("Ingrese el primer numero: \n"))
num2 = float(input("Ingrese el segundo numero: \n"))

if num2 != 0.0:
    print(str(num1) + " entre " + str(num2) + " = ", num1/num2)
else:
    print("¡ERROR! No divisible entre 0")
    
# SOLUCION DE https://aprendeconalf.es/
n = float(input("Introduce el dividendo: "))
m = float(input("Introduce el divisior: "))
if m == 0:
    print("¡Error! No se puede dividir por 0.")
else:
    print(n/m)
