#testei outra forma de colocar cores nesse programa
print('\033[1;36m' 'Printar primeiro e último nome' '\033[m') #titulo
cores = {'limpa': '\033[m', 'azul': '\033[1;34m', 'magenta': '\033[1;35m', 'verde':'\033[1;32m'}  #variável de cores para chamar pelo nome
nm = str(input('Digite seu nome completo: ')).strip().split()  #entrada do nome, separando por palavras e removendo espaços indesejados
print('Seu primeiro nome é:{}{}{}'.format(cores['azul'], nm[0], cores['limpa']))  #imprime primeiro nome
print("Seu último nome é:{}{}{}".format(cores['magenta'], nm[-1], cores['limpa']))  #imprime último nome
print("Seja bem vindo(a), {}{}{}!".format(cores['verde'], nm[0], cores['limpa']))  # bem vindo e primeiro nome da pessoa

