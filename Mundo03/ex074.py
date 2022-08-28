'''Exercício 074 - 
Crie um programa que vai gerar cinco números aleatórios e colocar em uma tupla.

Depois disso, mostre a listagem de números gerados e também indique o menor e o maior valor que
estão na tupla.'''

from random import randint

numeros = (randint(0, 20), randint(0, 20), randint(0, 20), randint(0, 20), randint(0, 20))
print(f'Tupla: {numeros}')
numeros = sorted(numeros)
print(f'O maior número é: {numeros[4]}\nO menor número é: {numeros[0]}')
