# JOSE ALFREDO ROMERO GONZALEZ 
# 08/10/2020
horasTrab = float(input("Numero de horas trabajadas: \n"))
costeHora = float(input("Cuanto te pagam por hora?: \n"))

print("La paga que le corresponde es: ", horasTrab * costeHora)

# SOLUCION  DE https://aprendeconalf.es/
horas = float(input("Introduce tus horas de trabajo: "))
coste = float(input("Introduce lo que cobras por hora: "))
paga = round(horas * coste, 3)
print("Tu paga es " + str(paga))
