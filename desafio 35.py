print('É UM TRIANGULO?')  # titulo
a = int(input('Digite o valor da primeira reta: '))  # entrada de valores das retas
b = int(input('Digite o valor da segunda reta: '))
c = int(input('Digite o valor da terceira reta: '))
if a < b + c and b < a + c and c < a + b: # para ser um triangulo é preciso que um de seus lados seja maior que a
    # soma dos outros dois
    print('\033[1;32mÉ um triângulo!\033[m')
else:
    print('\033[1;31mNão é um triângulo.\033[m')

