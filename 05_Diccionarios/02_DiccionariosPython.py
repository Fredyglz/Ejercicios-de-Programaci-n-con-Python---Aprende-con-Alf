# JOSE ALFREDO ROMERO GONZALEZ 
# 23/11/2020
dic_per = {'nombre': None, 'edad': None, 'direccion': None,'telefono': None}
for i in dic_per.keys():
    dic_per[i] = input("Ingrese su " + str(i) + ": ")

print(dic_per['nombre'] + " tiene " + dic_per['edad'] + " años, vive en " + dic_per['direccion'] + " y su número de teléfono es " + dic_per['telefono'] + ".")


# SOLUCION DE https://aprendeconalf.es/
name = input('¿Cómo te llamas? ')
age = input('¿Cuántos años tienes? ')
address = input('¿Cuál es tu dirección? ')
phone = input('¿Cuál es tu número de teléfono? ')
person = {'name': name, 'age': age, 'address': address, 'phone': phone}
print(person['name'], 'tiene', person['age'], 'años, vive en', person['address'], 'y su número de teléfono es', person['phone'])
