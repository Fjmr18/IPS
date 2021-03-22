# Computação Paralela e Distribuída 2020/2021–Lab 02
# Aluno1: (nome do aluno)(número do aluno)(turma do aluno)
# Aluno1: (nome do aluno)(número do aluno)(turma do aluno)
#############################################
import checkSys as check
print(check.get_processsor_info())

import random
def fibonacci(input):
    a, b = 0, 1
    for item in range(input):
        a, b = b, a + b
    print(f"F({input}) = {a}")

if __name__ == '__main__':
    valores = []
    for i in range(50):
        number=random.randint(0,100)
        valores.append(number)
    for val in valores:
        fibonacci(val)