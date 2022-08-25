print('\033[1;34m''Contagem de A' '\033[m')
frase = str(input('Digite uma frase: ')).upper().strip()  #coloca tudo no maiúsculo e remove espaços indesejados

print('A letra A aparece {}{}{} vezes '.format('\033[1;34m', frase.count('A'), '\033[m'))  # "count" contabiliza quanto A's a frase possui
print('A primeira letra A aparece na posição {}{}{} '.format('\033[1;31m', frase.find('A') +1, '\033[m')) # "find" retorna a primeira vez que a letra aparece na sentença
print('A ultima posição que a letra A aparece é {}{}{}'.format('\033[1;32m', frase.rfind('A')+1, '\033[m'))  # "rfind" retorna a última vez que a letra aparece na sentança
 # "+1" já que a contagem começa do 0, então temos que adicionar mais um
