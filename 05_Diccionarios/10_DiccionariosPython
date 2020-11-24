# JOSE ALFREDO ROMERO GONZALEZ 
# 23/11/2020
d_clientes = {}
print("********* CODEX'S Clients*********")
print("1 ------> Añadir cliente.")
print("2 ------> Eliminar cliente.")
print("3 ------> Mostrar cliente.")
print("4 ------> Listar todos los clientes.")
print("5 ------> Listas clientes preferentes.")
print("6 ------> Terminar.")

while True:
    op = input("Ingrese una opción: ")
    if op == '6':
        break
    elif op == '1':
        d_datos = {'Nombre':None, 'Dirección':None, 'Teléfono':None, 'Correo':None}
        nif = input("Ingrese el NIF del cliente: ")
        for i in d_datos.keys():
            d_datos[i] = input("Ingrese su " + str(i) + ": ")
        pref = input("Es un cliente preferente? (S/N): ")
        if pref == 'S':
            d_datos['Preferente'] = True
        elif pref == 'N':
            d_datos['Preferente'] = False
        d_clientes[nif] = d_datos
    elif op == '2':
        nif = input("Ingrese el NIF del cliente: ")
        if nif in d_clientes:
            del d_clientes[nif]
        else:
            print("¡ERROR! NIF inexistente")
    elif op == '3':
        nif = input("Ingrese el NIF del cliente: ")
        if nif in d_clientes:
            for p, v in d_clientes[nif].items():
             print(str(p) + ": " + str(v))
        else:
            print("¡ERROR! NIF inexistente")
    elif op == '4':
        for c in d_clientes:
            print(c, d_clientes[c]['Nombre'])
    elif op == '5':
        for c in d_clientes:
            if d_clientes[c]['Preferente'] == True:
                print(c, d_clientes[c]['Nombre'])
    else:
        print("¡ERROR! Opción no disponible")

# SOLUCION DE https://aprendeconalf.es/
clients = {}
option = ''
while option != '6':
    if option == '1':
        nif = input('Introduce NIF del cliente: ')
        name = input('Introduce el nombre del cliente: ')
        address = input('Introduce la dirección del cliente: ')
        phone = input('Introduce el teléfono del cliente: ')
        email = input('Introduce el correo electrónico del cliente: ')
        vip = input('¿Es un cliente preferente (S/N)? ')
        client = {'nombre':name, 'dirección':address, 'teléfono':phone, 'email':email, 'preferente':vip=='S'}
        clients[nif] = client
    if option == '2':
        nif = input('Introduce NIF del cliente: ')
        if nif in clients:
            del clients[nif]
        else:
            print('No existe el cliente con el nif', nif)
    if option == '3':
        nif = input('Introduce NIF del cliente: ')
        if nif in clients:
            print('NIF:', nif)
            for key, value in clients[nif].items():
                print(key.title() + ':', value)
        else:
            print('No existe el cliente con el nif', nif)
    if option == '4':
        print('Lista de clientes')
        for key, value in clients.items():
            print(key, value['nombre'])
    if option == '5':
        print('Lista de clientes preferentes')
        for key, value in clients.items():
            if value['preferente']:
                print(key, value['nombre'])
    option = input('Menú de opciones\n(1) Añadir cliente\n(2) Eliminar cliente\n(3) Mostrar cliente\n(4) Listar clientes\n(5) Listar clientes preferentes\n(6) Terminar\nElige una opción:')
