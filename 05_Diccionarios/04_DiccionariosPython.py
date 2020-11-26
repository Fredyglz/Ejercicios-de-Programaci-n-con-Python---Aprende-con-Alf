# JOSE ALFREDO ROMERO GONZALEZ 
# 23/11/2020
d_meses = {'01':'Enero', '02':'Febrero', '03':'Marzo', '04':'Abril', '05':'Mayo', '06':'Junio', '07':'Julio', '08':'Agosto', '09':'Septiembre', '10':'Octubre', '11':'Noviembre', '12':'Diciembre'}
fecha = input("Ingrese una fecha en formato dd/mm/aaaa: ")
fecha = fecha.split('/')
print(fecha[0], "de", d_meses[fecha[1]], "de", fecha[2])


# SOLUCION DE https://aprendeconalf.es/
months = {1:'enero', 2:'febrero', 3:'marzo', 4:'abril', 5:'mayo', 6:'junio', 7:'julio', 8:'agosto', 9:'septiembre', 10:'octubre', 11:'noviembre', 12:'diciembre'}
date = input('Introduce una fecha en formato dd/mm/aaaa: ')
date = date.split('/')
print(date[0], 'de', months[int(date[1])], 'de', date[2])
