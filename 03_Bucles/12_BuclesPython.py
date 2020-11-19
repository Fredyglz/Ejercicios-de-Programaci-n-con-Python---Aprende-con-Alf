# JOSE ALFREDO ROMERO GONZALEZ 
# 18/11/2020
frase = input("Ingrese una frase: \n")
letra = input("Ingrese una letra: \n")

# Forma 1
print(frase.count(letra))

# Forma 2
c = 0
for i in frase:
    if letra == i:
        c += 1
print(c)

# SOLUCION  DE https://aprendeconalf.es/
frase = input("Introduce una frase: ")
letra = input("Introduce una letra")
contador = 0
for i in frase:
    if i == letra:
        contador += 1
print("La letra '%s' aparece %2i veces en la frase '%s'." % (letra, contador, frase))
