# JOSE ALFREDO ROMERO GONZALEZ 
# 19/11/2020
l_m = ["Matemáticas", "Física", "Química", "Historia", "Idiomas"]
l_cal = []
for m in l_m:
    cal = float(input("Que calificacion obtuviste en " + str(m) + "?: "))
    l_cal.append([m, cal])
    
for m, cal in l_cal:
    if cal > 5:
        l_m.remove(m)
        
print("Las materias que tienes que repetir son: ", l_m)

# SOLUCION 1 DE https://aprendeconalf.es/
subjects = ["Matemáticas", "Física", "Química", "Historia", "Lengua"]
passed = []
for subject in subjects:
    score = float(input("¿Qué nota has sacado en " + subject + "?"))
    if score >= 5:
        passed.append(subject)
for subject in passed:
    subjects.remove(subject)
print("Tienes que repetir " + str(subjects))

# SOLUCION 2 DE https://aprendeconalf.es/
subjects = ["Matemáticas", "Física", "Química", "Historia", "Lengua"]
for i in range(len(subjects)-1, -1, -1):
    score = float(input("¿Qué nota has sacado en " + subjects[i] + "?"))
    if score >= 5:
        subjects.pop(i)
print("Tienes que repetir " + str(subjects))
