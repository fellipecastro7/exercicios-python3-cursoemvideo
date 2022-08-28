'''Exercício 031 - Custo da viagem
Desenvolva um programa que pergunte a distância de uma viagem em Km/h. Calcule o preço da passagem,
cobrando R$0,50 por Km/h para viagens de até 200Km e R$0,45 para viagens mais longas.'''

distancia = int(input('Informe a distância da viagem (EM KM/H): '))

if distancia <= 200:
    preco = 0.50 * distancia
    print(f'\nO preço da passagem é R${preco:.2f}')
else:
    preco = 0.45 * distancia
    print(f'\nO preço da passagem é R${preco:.2f}')
