'''Exercício 051 - Progressão Aritmética
Desenvolva um programa que leia o primeiro termo e a razão de uma PA. No final, mostre os 10
primeiros termos dessa progressão.'''

a1 = int(input('Informe o primeiro termo da PA: '))
razao = int(input('Informe a razão da PA: '))

a10 = a1 + (10 - 1) * razao

print(a1, end='  ')

for i in range(a1 + razao, a10 + razao, razao):
    print(i, end='  ')
