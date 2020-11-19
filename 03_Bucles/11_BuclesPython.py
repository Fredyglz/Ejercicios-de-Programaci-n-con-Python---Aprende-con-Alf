# JOSE ALFREDO ROMERO GONZALEZ 
# 18/11/2020
word = input("Ingrese una palabra: \n")
for i in reversed(word):
    print(i)

# SOLUCION  DE https://aprendeconalf.es/
word = input("Introduce una palabra: ")
for i in range(len(word)-1, -1, -1):
    print(word[i])
