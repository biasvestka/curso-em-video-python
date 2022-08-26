import random  #importa biblioteca "aleatória"
number = "012345"  #atribui quais números que sejam sorteados aleatoriamente
nmr = random.choice(number)  #sorteio
choose = input('Escolha um número de 0 a 5: ')  #escolher o número
if choose == nmr:  #se a escolha da pessoa for == ao sorteio:
    print('Você acertou!! :D')
else:
    print('Você errou... :(')
