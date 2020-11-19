# JOSE ALFREDO ROMERO GONZALEZ 
# 18/11/2020
inversion = float(input("Ingrese la cantidad a invertir: \n"))
ia = float(input("Ingrese el interes anual: \n"))
años = int(input("Ingrese la canitidad de años: \n"))

for i in range(años):
    inversion *= 1 + ia / 100
    print("La capital del año", i+1, "es de: ", round(inversion,2))
    
# SOLUCION DE https://aprendeconalf.es/
amount = float(input("¿Cantidad a invertir? "))
interest = float(input("¿Interés porcentual anual? "))
years = int(input("¿Años?"))
for i in range(years):
    amount *= 1 + interest / 100 
    print("Capital tras " + str(i+1) + " años: " + str(round(amount, 2)))
