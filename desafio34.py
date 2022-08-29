print('CALCULADORA AUMENTO DE SALÁRIO.')  # título
s = float(input("Digite seu salário: "))  # entrada do valor do salário
au1 = (10 / 100) * s + s  # porcentagem de 10% do salário
au2 = (15 / 100) * s + s  # porcentagem de 15% do salário
if s > 1250:  # se o salário for maior que 1.250,00 será 10% de aumento, senão 15%
    print('Seu salário total com aumento é {}R${}{}'.format('\033[4;34m', au1, '\033[m'))
else:
    print('Seu salário total com aumento é {}R${}{}'.format('\033[4;32m', au2, '\033[m'))
