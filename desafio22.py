print('\033[1;35m''Leitor de letras do seu nome.''\033[m')
nome = input('Insira seu nome completo: ').strip()
print('Seu nome em maiúsculo é', nome.upper())
print('Seu nome em minúsculo é', nome.lower())
nome1 = nome.replace(" ", "")
print('Seu nome completo tem {}{}{} letras.'.format('\033[1;34m', len(nome1), '\033[m'))
nome2 = nome.split()
print('Seu primeiro nome tem {}{}{} letras.'.format('\033[1;31m', len(nome2[0]), '\033[m'))

