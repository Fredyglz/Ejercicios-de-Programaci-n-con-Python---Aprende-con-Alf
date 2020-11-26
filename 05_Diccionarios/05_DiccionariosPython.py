# JOSE ALFREDO ROMERO GONZALEZ 
# 23/11/2020
d_boleta = {'Matemáticas':6, 'Física':4, 'Química': 5}
creditosTotal = 0
for m, c in d_boleta.items():
    creditosTotal += c
    print(m, "tiene", c, "créditos")
print("Créditos totales: ", creditosTotal)


# SOLUCION DE https://aprendeconalf.es/
course = {'Matemáticas': 6, 'Física': 4, 'Química': 5}
total_credits = 0
for subject, credits in course.items():
    print(subject, 'tiene', credits, 'créditos')
    total_credits += credits
print('Número total de créditos del curso: ', total_credits)
