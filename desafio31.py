print('VALOR POR VIAGEM')
distance = float(input('Insira a distância da viagem em KM: ')) #entrada da distância percorrida na viagem
pay = distance * 0.50  #se a distância for menor que 200km vc paga 0.50 por km
pay2 = distance * 0.45  #se a distância for maior que 200km vc paga 0.45 por km
if distance <= 200: #confere se a distância foir maior ou menor que 200
    print("O preço total a pagar é de {}R${}".format('\033[1;31m', pay))
else:
    print("O preco total a pagar é de {}R${}".format('\033[1;31m', pay2))
