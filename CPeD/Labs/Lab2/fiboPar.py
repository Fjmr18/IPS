# Computação Paralela e Distribuída 2020/2021
# Aluno: Fernando Ramalho 200290040 BS (BrightStart 2ª Edição)
# Aluno: Antonio Costa 200221097 (BrightStart 2ª Edição)
#############################################

from multiprocessing import Process, current_process
import checkSys as check, numpy as np
print(check.get_processsor_info())

rnd = np.random

def fibonacci(input):
    pnome = current_process().name
    a, b = 0, 1
    for item in range(input):
        a, b = b, a + b
    print(f"Process: {pnome}; F({a}) = {input}")

def randomizeNumbers(input):
    for i in input:
        randomNumber = rnd.randint(0, 100)
        fibonacci(randomNumber)

if __name__ == '__main__':
    processos = []
    for i in range(6):
        if (i == 0):
            numeros = range(8)
        elif (i == 1):
            numeros = range(12, 24)
        elif (i == 2):
            numeros = range(25, 48)
        elif (i == 3):
            numeros = range(49, 50)
        processo = Process(target=randomizeNumbers, args=(numeros,))
        processos.append(processo)
        processo.start()
    for processo in processos:
        processo.join()
    print("Multiprocessamento completo")