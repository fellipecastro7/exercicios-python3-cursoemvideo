'''Exercício 010 - Conversor de Moedas
Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos dólares ela
pode comprar.'''

real = float(input('Digite o dinheiro que você possui: R$'))

dolar = 4.80
euro = 5.29
jpy = 0.04
arg = 0.04

print(f'\nCom R${real:.2f}, você pode comprar US${real / dolar:.2f}')
print(f'Com R${real:.2f}, você pode comprar €{real / euro:.2f}')
print(f'Com R${real:.2f}, você pode comprar ¥{real / jpy:.2f}')
print(f'Com R${real:.2f}, você pode comprar ${real / arg:.2f}')
