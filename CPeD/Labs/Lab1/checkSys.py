# Computação Paralela e Distribuída 2020/2021
# Aluno: Fernando Ramalho 200290040 BS (BrightStart 2ª Edição)
# Aluno: Antonio Costa 200221097 (BrightStart 2ª Edição)
#############################################

import platform, subprocess
#O que é o Import: Processo de importação de codico composto por 2 fases: A procura do Modulo indicado, e a importação dele para o scope onde foi chamado.
#Modulo Platform: Utilizado para aceder a dados como Hardware, sistema operativo, e verção do interpretador
#Modulo Subprocess: Permite criar novas aplicações ou processos. Tambem utilizado para obter informação dee inputs, outputs e erros do pip.

# Função str(): A função str() permite converter caracters(Int's, floats etc) para strings, de modo a poder trabalhar com as strings. Por exemplo:

# x = 111                                                           x = 111
# y = "Hello world"                                                 y = "Hello world"
# print(x+y)                                                        print(str(x)+y)
#Output: Erro(Não é possivel somar int e str)                       Output: 111HelloWorld

# Função strip(): A função strip() remove os caracteres dados como argumento de ambas as pontas da string. Por exemplo:
# x = "123Hello World321"
# print(x.strip("1"))
# Output: 23Hello World32

def get_processsor_info():
    if platform.system() == "Windows":
        return platform.processor()
    elif platform.system() == "Darwin":
        return subprocess.check_output(['/usr/sbin/sysctl',"-n", "machdep.cpu.brand_string"]).strip()
    elif platform.system() == "Linux":
        command = "cat /proc/cpuinfo | grep name | cut -d ' ' -f 3-8"
        return str(subprocess.check_output(command, shell=True)).strip("b'\\n")
    return ""

if __name__ == '__main__':
    print(get_processsor_info())