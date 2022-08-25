print('\033[45m''Conferir se possui "Silva" como sobrenome''\033[m')  # titulo
nm = str(input('Digite seu nome completo: ')).strip()  # entrada do nome e "strip" para remover espaçoes indesejados
if "SILVA" in nm.upper():
    print("Você {}tem 'Silva'{} como sobrenome.".format('\033[3;33m', '\033[m'))  # se o sobrenome tiver SILVA, retornar mensagem dizendo que tem
else:
    print('Você {}não tem "Silva"{} como sobrenome.'.format('\033[3;31m', '\033[m'))  # se não tiver, retornar dizendo que não tem
