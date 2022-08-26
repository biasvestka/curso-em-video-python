print('CONFERIR SE O ANO DIGITADO É BISSEXTO')  #titulo
year = int(input('Digite um ano: '))  #entrada do ano
if year % 4 == 0:  #se o módulo do ano dividido por 4 for igual a 0:
    print('{}{}{} é ano bissexto!'.format('\033[7;36m', year, '\033[m'))
else:
    print('{}{}{} não é ano bissexto.'.format('\033[7;33m', year, '\033[m'))
