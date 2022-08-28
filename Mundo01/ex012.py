'''Exercício 012 - Calculando Descontos
Faça um programa que leia o preço de um produto e mostre seu novo preço, com 5% de desconto.'''

preco = float(input('Digite o preço do produto: R$'))

desconto = preco * (5 / 100)
preco_novo = preco - desconto

print(f'\nO desconto de 5% desse produto é de R${desconto:.2f}')
print(f'O novo preço do produto é de R${preco_novo:.2f}')
