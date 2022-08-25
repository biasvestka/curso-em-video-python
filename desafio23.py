print('\033[4;32m''Separar números por casas''\033[m')
dgt = int(input('Digite um número de 0 a 9999: '))
u = dgt // 1 % 10
d = dgt // 10 % 10
c = dgt // 100 % 10
m = dgt // 1000 % 10
print(dgt)
print('{}Unidade: {}.\nDezena: {}.\nCentena: {}.\nMilhar: {}.'.format('\033[1;32m', u, d, c, m, '\033[m'))
