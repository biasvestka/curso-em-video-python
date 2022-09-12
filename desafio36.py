print('APROVAÇÃO DE EMPRÉSTIMO')  # titulo
# se o valor parcela do imovel for maior que 30% do salário o empréstimo é negado.
hp = float(input('Insira o valor do imóvel: '))
s = float(input('Insira o seu salário: '))
y = int(input('Insira em quantos anos irá pagar: '))
p = float(hp/(y*12))  # parcela
pcnt = (s*30)/100  # porcentagem 30% salário

if p > pcnt:  # se a parcela for maior que o 30%, negado
    print('Empréstimo negado.')
else:  # senão, aprovado
    print('Empréstimo aprovado! Parcelas de R${:.2f} mensais por {} anos.'.format(p, y))










