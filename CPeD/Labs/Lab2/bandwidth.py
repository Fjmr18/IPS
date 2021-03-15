#Computação Paralela e Distribuída 2020/2021–Lab 01
#Aluno: Fernando Ramalho 200290040 BS (BrightStart 2ª Edição)
#Aluno: Antonio Costa 200221097 (BrightStart 2ª Edição)
#############################################

import checkSys as check, timeit, numpy as np
print(check.get_processsor_info())
rnd = np.random
bwRAM = []                                             # Lista para a media de tempos
n = [1000, 10000, 100000,                              # Lista de numeros
     1000000, 10000000, 20000000]

for n in n:                                            # Ciclo for para percorrer a lista dos numeros
    soma = 0.0
    vetor = rnd.uniform(0,1000,size=n)
    melhorTempo = 9999999                              # Aleatoriamente grande
    for i in range(3):                                 # Efetua 3 medições de tempo e mostra a melhor
        print(f"Medição {i+1} para {n} elementos...")
        starttime = timeit.default_timer()
        for j in range(n):
            soma += vetor[j]
        tempo = timeit.default_timer() - starttime
        bwRAM.append(tempo)                           #Append(tempo) para adicionar o tempo à lista bwRAM
        if (tempo < melhorTempo):
            melhorTempo = tempo
    print(f"Melhor tempo da soma para {n} elementos: {melhorTempo} segundos")
    print(f"Largura de banda da RAM: {n*4/melhorTempo/1000000:.2f} Mega Bytes por segundo")
    print(f"A media dos tempos é: {sum(bwRAM)/len(bwRAM)}")         # Print da media de tempos