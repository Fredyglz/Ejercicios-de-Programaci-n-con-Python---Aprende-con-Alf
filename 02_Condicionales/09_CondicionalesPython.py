# JOSE ALFREDO ROMERO GONZALEZ 
# 12/10/2020
edad = int(input("Ingrese su edad para entrar a la diversión!: \n"))

if edad < 4:
    precio = 0.0
elif edad <= 18:
    precio = 5.0
else:
    precio = 10.0
    
print("El cliente debe pagar " + str(precio) + "$")

# SOLUCION DE https://aprendeconalf.es/
edad = int(input("Introduce tu edad: "))
# Decisión del precio en función de la edad
if edad < 4:
    precio = 0
elif edad <= 18:
    precio = 4
else:
    precio = 10
# Mostrar precio
print("El precio de la entrada es", precio, "€.")
