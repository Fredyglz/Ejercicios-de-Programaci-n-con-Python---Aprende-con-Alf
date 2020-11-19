# JOSE ALFREDO ROMERO GONZALEZ 
# 08/10/2020
precioHabitual = 3.49
descuento = .6
vendidas = int(input("Ingrese el numero de barras vendidas que no son del dia: \n"))

precioTotal = (precioHabitual * (1-descuento)) * vendidas 

print("Precio normal: ", precioHabitual, "Descuento: ", descuento * 100, "% Precio con descuento: ", precioHabitual * descuento, "Coste final total: ", precioTotal )

# SOLUCION  DE https://aprendeconalf.es/
barras = int(input("Introduce el número de barras vendidas que no son frescas: "))
precio = 3.49 
descuento = 0.6
coste = barras * precio * (1 - descuento)
print("El coste de una barra fresca es " + str(precio) + "€")
print("El descuento sobre una barra no fresca es " + str(descuento * 100) + "%")
print("El coste final a pagar es " + str(round(coste, 2)) + "€")
