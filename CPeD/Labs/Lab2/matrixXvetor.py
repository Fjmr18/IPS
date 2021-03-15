# Computação Paralela e Distribuída 2020/2021–Lab 01
# Aluno: Fernando Ramalho 200290040 BS (BrightStart 2ª Edição)
# Aluno: Antonio Costa 200221097 (BrightStart 2ª Edição)
#############################################

import timeit, numpy as np
rnd = np.random
n = 500
matriz1 = rnd.uniform(0, 500, size=(n, n))
matriz2 = rnd.uniform(0, 500, size=(n, n))
resultado = np.zeros((n,n))
starttime = timeit.default_timer()

for i in range(len(matriz1)):                        # numero de linhas da matriz
    for j in range(len(matriz2)):                     # numero de elementos no vetor
        temp = 0
        for k in range(len(matriz2)):
            temp += matriz1[i,k]*matriz2[k,j]
        resultado[i,j] = temp
print(f"Tempo 1: {timeit.default_timer() - starttime}")
print(f"Primeiro elemento da matriz resultado: {resultado[0][0]}")
starttime = timeit.default_timer()
resultado = np.matmul(matriz1,matriz2)
print(f"Tempo 2: {timeit.default_timer() - starttime}")
print(f"Primeiro elemento da matriz resultado: {resultado[0][0]}")