# Computação Paralela e Distribuída 2020/2021–Lab 01
# Aluno: Fernando Ramalho 200290040 BS (BrightStart 2ª Edição)
# Aluno: Antonio Costa 200221097 (BrightStart 2ª Edição)
#############################################

import timeit, numpy as np
rnd = np.random
n = 500
vetorB = rnd.uniform(0, 1000, size=(n, n))
matriz = rnd.uniform(0, 1000, size=(n, n))
resultado = np.zeros((n,n))
starttime = timeit.default_timer()
resultado = np.matmul(vetorB,matriz)
print(f"Tempo: {timeit.default_timer() - starttime}")
print(f"Primeiro elemento do vetor resultado: {resultado[0,0]}")

resultado = np.zeros((n,n))
for i in range(len(matriz)):                        # numero de linhas da matriz
    for j in range(len(vetorB)):                     # numero de elementos no vetor
        resultado[i,j] += matriz[i,j]*vetorB[i,j]
print(f"Primeiro elemento do vetor resultado (Metedo anterior): {resultado[0,0]}")