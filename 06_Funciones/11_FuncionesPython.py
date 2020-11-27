# JOSE ALFREDO ROMERO GONZALEZ 
# 26/11/2020
def diccionarioPalabras(frase):
    l_palabras = frase.split()
    d_palabras = {}
    for p in l_palabras:
        if p not in d_palabras:
            d_palabras[p] = 1
        else:
            d_palabras[p] += 1
    return d_palabras

def tuplaPalabra(frase):
    d_palabras = diccionarioPalabras(frase)
    print(d_palabras)
    cantidad = 0
    for k, v in d_palabras.items():
        if v > cantidad:
            cantidad = v
            palabra = k
    return palabra, cantidad
    
print(tuplaPalabra("Como quieres que te quiera si el que quiero que me quiera no me quiere como quiero que me quiera"))

# SOLUCION DE https://aprendeconalf.es/
def count_words(text):
    """Función que cuenta el número de veces que aparece cada palabra en un texto.
    Parámetros:
        - text: Es una cadena de caracteres.
    Devuelve: 
        Un diccionario con pares palabra:frecuencia con las palabras contenidas en el texto y su frecuencia.
    """
    text = text.split()
    words = {}
    for i in text:
        if i in words:
            words[i] += 1
        else:
            words[i] = 1
    return words

def most_repeated(words):
    max_word = ''
    max_freq = 0
    for word, freq in words.items():
        if freq > max_freq:
            max_word = word
            max_freq = freq
    return max_word, max_freq

text = 'Como quieres que te quiera si el que quiero que me quiera no me quiere como quiero que me quiera'
print(count_words(text))
print(most_repeated(count_words(text)))
