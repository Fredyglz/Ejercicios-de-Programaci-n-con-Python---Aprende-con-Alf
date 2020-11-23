# JOSE ALFREDO ROMERO GONZALEZ 
# 23/11/2020
my_d = {'Euro':'€', 'Dollar':'$', 'Yen':'¥'}
divisa =  input("Ingrese una divisa: ")
if divisa in my_d:
    print(divisa, ":", my_d[divisa])
else:
    print("La divisa no se encuentra registrada")

# SOLUCION DE https://aprendeconalf.es/
currencies = {'Euro':'€', 'Dollar':'$', 'Yen':'¥'}
currency = input("Introduce una divisa: ")
print(currencies.get(currency.title(), "La divisa no está."))
