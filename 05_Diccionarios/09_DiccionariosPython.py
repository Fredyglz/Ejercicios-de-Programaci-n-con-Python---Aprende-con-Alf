# JOSE ALFREDO ROMERO GONZALEZ 
# 23/11/2020
d_f = {}
cantidadCobrada = 0
cantidadPendiente = 0
print("********* FACTURAS *********")
print("1 -------> Agregar factura")
print("2 -------> Pagar factura")
print("3 -------> Salir")
print("Cobrado:", cantidadCobrada)
print("Pendiente:", cantidadPendiente) 

while True:
    op = int(input("Ingrese una opcion: "))
    if op == 3:
        break
    elif op == 1:
        numero = int(input("Ingrese el numero de la factura: "))
        costo = float(input("Ingrese el costo de la factura: "))
        d_f[numero] = costo
        cantidadPendiente += costo
    elif op == 2:
        numero = int(input("Ingrese el numero de la factura a pagar: "))
        cantidadCobrada += d_f[numero]
        cantidadPendiente -= d_f[numero]
        del d_f[numero]
    else:
        print("¡ERROR! Ingrese una opcion valida")
        continue
    print("Cobrado:", cantidadCobrada)
    print("Pendiente:", cantidadPendiente) 

# SOLUCION DE https://aprendeconalf.es/
invoices = {}
collected = 0
remains = 0
more = ''
while more != 'T':
    if more == 'A':
        key = input('Introduce el número de la factura: ')
        cost = float(input('Introduce el coste de la factura: '))
        invoices[key] = cost
        remains += cost
    if more == 'P':
        key = input('Introduce el número de la factura a pagar: ')
        cost = invoices.pop(key, 0)
        collected += cost
        remains -= cost
    print('Recaudado:', collected)
    print('Pendiente de cobro: ', remains)
    more = input('¿Quieres añadir una nueva factura (A), pagarla (P) o terminar (T)? ')

