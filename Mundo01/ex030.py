'''Exercício 030 - Par ou ímpar?
Crie um programa que leia um número inteiro e mostre na tela se ele é PAR ou ÍMPAR.'''

num = int(input('Informe um número: '))

paridade = num % 2

if paridade == 0:
    print(f'\nO número {num} é par.')
else:
    print(f'\nO número {num} é ímpar.')
