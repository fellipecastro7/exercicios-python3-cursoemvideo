'''Exercício 019 - Sorteando um item na Lista
Um professor que sortear um dos seus quatro alunos para apagar o quadro. Faça um programa que ajude
ele, lendo o nome deles e escrevendo o nome do escolhido.'''

from random import choice
a1 = input('Informe o nome do primeiro aluno: ')
a2 = input('Informe o nome do segundo aluno: ')
a3 = input('Informe o nome do terceiro aluno: ')
a4 = input('Informe o nome do quarto aluno: ')

l = [a1, a2, a3, a4]
e = choice(l)

print(f'\nO aluno escolhido foi: {e}')
