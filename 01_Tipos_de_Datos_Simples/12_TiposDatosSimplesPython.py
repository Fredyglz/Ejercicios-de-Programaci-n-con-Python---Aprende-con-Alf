# JOSE ALFREDO ROMERO GONZALEZ 
# 08/10/2020
payasos = int(input("Ingresa el numero de payasos vendidos: \n"))
muñecas = int(input("Ingresa el numero de muñecas vendidas: \n"))

pesoTotal = (112 * payasos) + (75 * muñecas)

print("El peso total es de " + str(pesoTotal ))

# SOLUCION  DE https://aprendeconalf.es/
peso_payaso = 112
peso_muñeca = 75
payasos = int(input("Introduce el número de payasos a enviar: "))
muñecas = int(input("Introduce el número de muñecas a enviar: "))
peso_total = peso_payaso * payasos + peso_muñeca * muñecas
print("El peso total del paquete es " + str(peso_total))
