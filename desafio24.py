print('\033[44m'"Conferir se o nome de uma cidade começa com 'Santo'"'\033[m')
city = str(input('Digite o nome de uma cidade: ')).strip()
if city[:5].upper() == 'SANTO':
    print('{}Começa{} com "Santo".'.format('\033[4;32m', '\033[m'))
else:
    print('{}Não{} começa com "Santo".'.format('\033[4;31m', '\033[m'))
