# JOSE ALFREDO ROMERO GONZALEZ 
# 08/10/2020
peso = float(input("Ingresa tu peso en kg: \n"))
estatura = float(input("Ingresa tu estatura en metros: \n"))
imc = round((peso / estatura ** 2 ), 2)

print("Tu índice de masa corporal es " + str(imc))

# SOLUCION  DE https://aprendeconalf.es/
weight = input("¿Cuál es tu peso en kg? ")
height = input("¿Cuál es tu estatura en metros?")
bmi = round(float(weight)/float(height)**2,2)
print("Tu índice de masa corporal es " + str(bmi))
