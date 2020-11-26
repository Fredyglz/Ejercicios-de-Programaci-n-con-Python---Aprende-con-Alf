# JOSE ALFREDO ROMERO GONZALEZ 
# 19/11/2020

# SOLUCION 1
l_precios = [50, 75, 46, 22, 80, 65, 8]
p_min = l_precios[0]
p_max = l_precios[0]
for p in l_precios:
    if p < p_min:
        p_min = p
    if p > p_max:
        p_max = p
print("El precio mas grande es:", p_max)
print("El precios menos grande es:", p_min)

# SOLUCION 2
print("El precio mas grande es:", max(l_precios))
print("El precios menos grande es:", min(l_precios))


# SOLUCION DE https://aprendeconalf.es/
prices = [50, 75, 46, 22, 80, 65, 8]
min = max = prices[0]
for price in prices:
    if price < min:
        min = price
    elif price > max:
        max = price 
print("El mínimo es " + str(min)) 
print("El máximo es " + str(max))
