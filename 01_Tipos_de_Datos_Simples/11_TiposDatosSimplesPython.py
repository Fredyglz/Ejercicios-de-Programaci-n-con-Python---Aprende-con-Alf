# JOSE ALFREDO ROMERO GONZALEZ 
# 08/10/2020
inversion = float(input("Ingrese la cantidad a invertir: \n"))
interes = float(input("Ingrese el interes anual: \n"))
años = float(input("Ingrese el numero de años: \n"))

capital = inversion * (interes / 100 + 1) ** años

print("El capital obtenido de la inversion es: " + str(round(capital, 2)))

# SOLUCION  DE https://aprendeconalf.es/
amount = float(input("¿Cantidad a invertir? "))
interest = float(input("¿Interés porcentual anual? "))
years = int(input("¿Años?"))
print("Capital final: " + str(round(amount * (interest / 100 + 1) ** years, 2)))
