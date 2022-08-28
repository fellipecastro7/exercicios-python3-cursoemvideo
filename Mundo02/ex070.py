'''Exercício 070 - Estatísticas em produtos
Crie um programa que leia o nome e o preço de vários produtos. O programa deverá perguntar se o
usuário vai continuar. No final, mostre:

A) Qual é o total gasto na compra.
B) Quantos produtos custam mais de R$1000.
C) Qual é o nome do produto mais barato'''

print('=-' * 13)
print('\tCOMPRAS')
print('=-' * 13)

total = mais1000 = 0
produtos = {}

while True:
    nome = input('Insira o nome do produto: ').strip()
    preco = float(input('Insira o preço do produto: R$'))

    while preco < 0:
        preco = float(input('Insira o preço do produto: '))

    produtos[nome] = preco

    if preco > 1000:
        mais1000 += 1

    total += preco
    opcao = input('\nDeseja continuar? [S / N] ').strip().upper()

    while opcao not in 'SN':
        opcao = input('\nDeseja continuar? [S / N] ').strip().upper()

    if opcao == 'N':
        break

print(f'\nTotal gasto na compra: R${total:.2f}')
print(f'{mais1000} produtos custam mais de R$1000.00')
print(f'{min(produtos, key=produtos.get)} é o produto mais barato e custa R${min(produtos.values()):.2f}')
