# JOSE ALFREDO ROMERO GONZALEZ 
# 08/10/2020
dinero = float(input("Ingrese la cantidad de dinero: \n"))

primerAño = round(dinero + (dinero * .04), 2)
segundoAño = round(primerAño + (primerAño * .04), 2)
tercerAño = round(segundoAño + (segundoAño * .04), 2)

print("Primer año: ", primerAño)
print("Segundo año: ", segundoAño)
print("Tercer año: ", tercerAño)

# SOLUCION  DE https://aprendeconalf.es/
inversion = float(input("Introduce la inversión inicial: "))
interes = 0.04
balance1 = inversion * (1 + interes)
print("Balance tras el primer año:" + str(round(balance1, 2)))
balance2 = balance1 * (1 + interes)
print("Balance tras el segundo año:" + str(round(balance2, 2)))
balance3 = balance2 * (1 + interes)
print("Balance tras el tercer año:" + str(round(balance3, 2)))
