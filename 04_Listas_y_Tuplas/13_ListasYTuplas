# JOSE ALFREDO ROMERO GONZALEZ 
# 19/11/2020
nums = input("Ingrese numeros separados por comas (sin espacios): ")
nums = nums.split(",")
l_nums = []
for num in nums:
    l_nums.append(int(num))
media = sum(l_nums)/len(l_nums)

acum = 0
for num in l_nums:
    acum += (num-media)**2
desviacion = (acum/len(l_nums))**(1/2)
print("Media", media)
print("Desviación estandar", desviacion)

# SOLUCION DE https://aprendeconalf.es/
sample = input("Introduce una muestra de números separados por comas: ")
sample = sample.split(',')
n = len(sample)
for i in range(n):
    sample[i] = int(sample[i])
sample = tuple(sample)
sum = 0
sumsq = 0
for i in sample:
    sum += i
    sumsq += i**2
mean = sum/n
stdev = (sumsq/n-mean**2)**(1/2)
print('La media es', mean, ', y la desviación típica es', stdev)
