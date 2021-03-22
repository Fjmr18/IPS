# Computação Paralela e Distribuída 2020/2021
# Aluno: Fernando Ramalho 200290040 BS (BrightStart 2ª Edição)
# Aluno: Antonio Costa 200221097 (BrightStart 2ª Edição)
#############################################
import time

COUNT = 50000000

def countdown(n):
    while n>0:
        n -= 1

start = time.time()
countdown(COUNT)
end = time.time()
print(f"Tempo em segundos: {end-start}")