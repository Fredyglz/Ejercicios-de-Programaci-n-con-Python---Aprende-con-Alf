# JOSE ALFREDO ROMERO GONZALEZ 
# 19/11/2020
v_a = ((1, 2, 3), (4, 5, 6))
v_b = ((-1, 0), (0, 1), (1, 1))
v_r = []
for r_a in v_a:
    l_acum = []
    for ite in range(len(v_a)):
        acum = 0
        for e in range(len(v_b)):
            acum += v_b[e][ite] * r_a[e]  
        l_acum.append(acum)
    v_r.append(tuple(l_acum))

v_r = tuple(v_r)
print(v_r)

# SOLUCION DE https://aprendeconalf.es/
a = ((1, 2, 3),
     (4, 5, 6))
b = ((-1, 0),
     (0, 1),
     (1,1))
result = [[0,0],
          [0,0]]
for i in range(len(a)):
    for j in range(len(b[0])):
        for k in range(len(b)):
            result[i][j] += a[i][k] * b[k][j]
for i in range(len(result)):
    result[i] = tuple(result[i])
result = tuple(result)
for i in range(len(result)):
    print(result[i])
