# JOSE ALFREDO ROMERO GONZALEZ 
# 23/11/2020
d_f = {'Plátano':1.35, 'ManManznazana':0.80, 'Pera':0.85, 'Naranja':0.70}
fruta = input("Ingrese una fruta: ")
if fruta in d_f:
    kilos = int(input("Ingrese cuantos kilos quiere: "))
    print(kilos, "kilos de", fruta, "= $", kilos*d_f[fruta])
else:
    print("Fruta no disponible, tonto")


# SOLUCION DE https://aprendeconalf.es/
fruits = {'Plátano':1.35, 'Manzana':0.8, 'Pera':0.85, 'Naranja':0.7}
fruit = input('¿Qué fruta quieres? ').title()
kg = float(input('¿Cuántos kilos? '))
if fruit in fruits:
    print(kg, 'kilos de', fruit, 'valen', fruits[fruit]*kg )
else: 
    print("Lo siento, la fruta", fruit, "no está disponible.")
