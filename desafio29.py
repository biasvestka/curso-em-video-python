print('\033[4;33m''Verificador de velocidade''\033[m')  #titulo
speed = float(input('Digite a velocidade do carro: ')) #entrada da velocidade do veículo
ticket = (speed - 80) * 7  #a multa é a velocidade do carro menos(-) a permitida (80), vezes(*) 7
if speed > 80: #se a velocidade foi maior do que a permitida vai a aparecer a msg do valor da multa
    print('{}Você foi multado por ultrapassar o limite de velocidade, no total de R${}{}'.format('\033[1;31m', ticket, '\033[m'))
else:
    print('{}Parabéns!{} Você andou na velocidade correta.'.format('\033[1;32m', '\033[m')) #senão, parabeniza
