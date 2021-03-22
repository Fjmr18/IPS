# Computação Paralela e Distribuída 2020/2021
# Aluno: Fernando Ramalho 200290040 BS (BrightStart 2ª Edição)
# Aluno: Antonio Costa 200221097 (BrightStart 2ª Edição)
#############################################

from multiprocessing import Pool
from timeit import default_timer as timer
import numpy as np
def createandsort (n):
    rand = np.random.RandomState(42)
    a = rand.rand(n)  # Gera um vetor de tamanho n
    return a.sort()  # Ordena o vetor

def sort_seq(sizes):
    tic = timer()
    [createandsort(size) for size in sizes]
    tac = timer()
    print(f"Tempo para ordenação sequencial: {tac -tic:21.8f}")

def sort_par(sizes):
    pool = Pool(processes=4)  # Use o número de cores físicos da sua máquina
    tic = timer()
    pool.map(createandsort, sizes)
    tac = timer()
    print(f"Tempo para ordenação paralela:{tac - tic:21.8f}")

if __name__ == "__main__":
    for i in [10, 10 ** 3, 10 ** 4, 10 ** 5, 10 ** 6, 5 * 10 ** 6, 10 ** 7]:
        sizes = [i for j in range(3)]
        print(f"\nNumero de elementos dos vetores a ordenar : {i}")

        # ordenaçãoem processamento sequencial
        sort_seq(sizes)

        # ordenação em processamento paralelo
        sort_par(sizes)