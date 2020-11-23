# JOSE ALFREDO ROMERO GONZALEZ 
# 23/11/2020
d_c = {}
while True:
    producto = input("Ingrese el nombre del artículo (enter para terminar): ")
    if producto == "":
        break
    precio = float(input("Ingrese el precio del artículo: $"))
    d_c[producto] = precio

print("Lista de la compra")
total = 0
for a, p in d_c.items():
    total += p
    print(a, "\t", p)
print("------------------")
print("Total: \t", total)



# SOLUCION DE https://aprendeconalf.es/
basket = {}
more = 'Si'
while more == 'Si':
    item = input('Introduce un artículo: ')
    price = float(input('Introduce el precio de ' + item + ': '))
    basket[item] = price
    more = input('¿Quieres añadir artículos a la lista (Si/No)? ')
cost = 0
print('Lista de la compra')
for item, price in basket.items():
    print(item, '\t', price)
    cost += price
print('Coste total: ', cost)
