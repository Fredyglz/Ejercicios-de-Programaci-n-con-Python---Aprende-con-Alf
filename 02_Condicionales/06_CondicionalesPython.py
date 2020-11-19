# JOSE ALFREDO ROMERO GONZALEZ 
# 12/10/2020
nombre = input("Ingresa tu edad: \n")
sexo = input("Ingresa tu sexo(h/m): \n")

if (sexo == 'm' and nombre[0] < 'M') or (sexo == 'h' and nombre[0] > 'N'):
    print("Grupo A")
else:
    print("Grupo B")
    
# SOLUCION 1 DE https://aprendeconalf.es/
name = input("¿Cómo te llamas? ")
gender = input("¿Cuál es tu sexo (M o H)? ")
if gender == "M":
    if name.lower() < "m":
        group = "A"
    else:
        group = "B"
else:
    if name.lower() > "n":
        group = "A"
    else:
        group = "B"
print("Tu grupo es " + group)

# SOLUCION 2 DE https://aprendeconalf.es/
name = input("¿Cómo te llamas? ")
gender = input("¿Cuál es tu sexo (M o H)? ")
if (gender == "M" and name.lower() < 'm') or (gender == "H" and name.lower() > 'n'):
    group = "A"
else:
    group = "B"
print("Tu grupo es " + group)
