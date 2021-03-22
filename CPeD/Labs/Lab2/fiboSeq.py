# Computação Paralela e Distribuída 2020/2021
# Aluno: Fernando Ramalho 200290040 BS (BrightStart 2ª Edição)
# Aluno: Antonio Costa 200221097 (BrightStart 2ª Edição)
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