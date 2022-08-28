'''Exercício 020 - Sorteando uma ordem na lista
O mesmo professor do desafio anterior quer sortear a ordem de apresentação de trabalhos dos alunos.
Faça um programa que leia o nome dos quatro alunos e mostre a ordem sorteada.'''

from random import shuffle
a1 = input('Informe o nome do primeiro aluno: ')
a2 = input('Informe o nome do segundo aluno: ')
a3 = input('Informe o nome do terceiro aluno: ')
a4 = input('Informe o nome do quarto aluno: ')

l = [a1, a2, a3, a4]
shuffle(l)

print(f'\nA ordem sorteada é:\n{l}')
