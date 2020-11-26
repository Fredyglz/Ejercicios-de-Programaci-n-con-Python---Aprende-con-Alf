# JOSE ALFREDO ROMERO GONZALEZ 
# 26/11/2020
def areaCirculo(r):
    return 3.14159 * (r**2)

def volumenCilindro(r, h):
    A = areaCirculo(r)
    return A*h

r = 3
h = 5
A = areaCirculo(r)
V = volumenCilindro(r, h)

print("Area del circulo:", A)
print("Volumen del circulo:", V)

# SOLUCION DE https://aprendeconalf.es/
def circle_area(radius):
    """Función que calcula el area de un círculo.
    Parámetros
    radius: Es el radio del círculo.
    Devuelve el área del círculo de radio radius. 
    """
    pi = 3.1415
    return pi*radius**2

def cilinder_volume(radius, high):
    """Función que calcula el volumen de un cilindro.
    Parámetros
    radius: Es el radio de la base del cilindro.
    high: Es la altura del cilindro.
    Devuelve el volumen del clindro de radio radius y altura high.
    """
    return circle_area(radius)*high

print(cilinder_volume(3,5))
