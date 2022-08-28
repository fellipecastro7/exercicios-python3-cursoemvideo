'''Exercício 023 - Separando dígitos de um número
Faça um programa que leia de 0 a 9999 e mostre na tela cada um dos dígitos separados.'''

num = int(input('Informe um número (de 0 a 9999): '))

unidade = num // 1 % 10
dezena = num // 10 % 10
centena = num // 100 % 10
milhar = num // 1000 % 10

print(f'\nUnidade: {unidade:.0f}')
print(f'Dezena: {dezena}')
print(f'Centena: {centena}')
print(f'Milhar: {milhar}')
