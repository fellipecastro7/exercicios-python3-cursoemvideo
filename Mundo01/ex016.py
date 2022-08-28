'''Exercício 016 - Quebrando um Número
Crie um programa que leia um número real pelo teclado e mostre na tela a sua porção inteira.'''

from math import trunc
num = float(input('Informe um número: '))
print(f'\nO número digitado foi {num} e a sua porção inteira é {trunc(num)}.')
