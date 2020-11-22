# JOSE ALFREDO ROMERO GONZALEZ 
# 19/11/2020
frase = input("Ingresa una frase: ")
frase = frase.lower()
frase = frase.split()
fraseConvertida = ""
palindromo = True

for l in frase:
    fraseConvertida += l

for l in range(len(fraseConvertida)):
    if fraseConvertida[l] != fraseConvertida[-l-1]:
        palindromo = False
        break

if palindromo:
    print("Es un palíndromo")
else:
    print("No es un palíndromo")

# SOLUCION DE https://aprendeconalf.es/
word = input("Introduce una palabra: ")
reversed_word = word
word = list(word)
reversed_word = list(reversed_word)
reversed_word.reverse()
if word == reversed_word:
    print("Es un palíndromo")
else:
    print("No es un palíndromo")
