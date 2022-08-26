print('\033[1;32m' 'Conferir se um número é ímpar ou par''\033[m')  #titulo
nm = int(input('Digite um número inteiro: '))  #entrada do número inteiro
div = nm % 2  #pega o número inserido e faz módelo de 2
if div == 0:   #todo número par é divisivel por 2 e com resto zero
    print('\033[1;34m''É par!''\033[m')
else:
    print('\033[1;32m''Não é par!''\033[m')

