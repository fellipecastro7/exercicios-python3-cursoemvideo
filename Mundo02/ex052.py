'''Exercício 052 - Números primos
Faça um programa que leia um número inteiro e diga se ele é ou não um número primo.'''

num = int(input('Informe um número: '))

primo = 0

for i in range(1, num + 1):
    if num % i == 0:
        primo += 1
if primo == 2:
    print(f'{num} é um número primo.')
else:
    print(f'{num} não é um número primo.')
