# JOSE ALFREDO ROMERO GONZALEZ 
# 23/11/2020
d_esEn = {}
while True:
    pEspañol = input("Ingrese una palabra en español (enter para terminar): ")
    if pEspañol == "":
        break
    d_esEn[pEspañol] = input("Ingrese la traduccion de " + pEspañol + ": ")

frase = input("Ingrese una frase: ")
frase = frase.split()
for p in frase:
    if p in d_esEn:
        print(d_esEn[p], end=" ")
    else:
        print(p, end=" ")



# SOLUCION DE https://aprendeconalf.es/
dictionary = {}
words = input("Introduce la lista de palabras y traducciones en formato palabra:traducción separadas por comas: ")
for i in words.split(','):
    key, value = i.split(':')
    dictionary[key] = value
phrase = input('Introduce una frase en español: ')
for i in phrase.split():
    if i in dictionary:
        print(dictionary[i], end=' ')
    else:
        print(i, end=' ')
