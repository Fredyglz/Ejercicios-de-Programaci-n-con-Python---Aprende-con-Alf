# JOSE ALFREDO ROMERO GONZALEZ 
# 12/10/2020
edad = int(input("Ingrese su edad: \n"))
ingreso = float(input("Ingrese sus ingresos mensuales: \n"))

if edad > 16 and ingreso >= 1000.0:
    print("Usted tiene que tributar")
else:
    print("Usted no tiene que atributar")
    
# SOLUCION 1 DE https://aprendeconalf.es/
age = int(input("¿Cuál es tu edad? "))
income = float(input("¿Cuales son tus ingresos mensuales?"))
if age > 16 and income >= 1000:
    print("Tienes que cotizar")
else:
    print("No tienes que cotizar")

# SOLUCION 2 DE https://aprendeconalf.es/
age = int(input("¿Cuál es tu edad? "))
income = float(input("¿Cuales son tus ingresos mensuales?"))
if age <= 16 or income < 1000:
    print("No tienes que cotizar")
else:
    print("Tienes que cotizar")
