# JOSE ALFREDO ROMERO GONZALEZ 
# 12/10/2020
renta = float(input("Ingrese su renta anual: \n"))

if renta < 10000.0:
    impositivo = 5
elif renta >= 10000 and renta < 20000:
    impositivo = 15
elif renta >= 20000 and renta < 35000:
    impositivo = 20
elif renta >= 35000 and renta < 60000:
    impositivo = 30
else:
    impositivo = 45

print("Le corresponde un impositivo de " + str(impositivo) + "%")

# SOLUCION DE https://aprendeconalf.es/
income = float(input("¿Cuál es tu renta anual? "))
if income < 10000:
    tax = 5
elif income < 20000:
    tax = 15
elif income < 35000:
    tax = 20
elif income < 60000:
    tax = 30
else:
    tax = 45
print("Tu tipo impositivo es " + str(tax) + "%")
