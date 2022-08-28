'''Exercício 029 - Radar eletrônico
Escreva um programa que leia a velocidade de um carro.
Se ele ultrapassar 80Km/h, mostre uma mensagem dizendo que ele foi multado.
A multa vai custar R$7,00 por cada Km acima do limite.'''

velocidade = int(input('Informe a velocidade do carro (EM KM/H): '))

if velocidade > 80:
    print('\nA velocidade informada ultrapassou o limite de 80Km/h. VOCÊ FOI MULTADO!')
    multa = 7.00 * (velocidade - 80)
    print(f'Multa: R${multa:.2f}')
else:
    print('\nA velocidade informada está no limite de 80Km/h.')
