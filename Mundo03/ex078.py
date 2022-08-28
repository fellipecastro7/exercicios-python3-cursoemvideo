'''Exercício 078 - Maior e Menor valores na Lista
Faça um programa que leia 5 valores numéricos e guarde-os em uma lista. No final, mostre qual foi o
maior e o menor valor digitado e as suas respectivas posições na lista.'''

lista = []

for i in range(5):
    num = int(input('Insira um número: '))
    lista.append(num)

print(f'Lista gerada: {lista}')
print(f'O maior valor é {max(lista)} e se encontra nas posições ', end='')

for i, v in enumerate(lista):
    if v == max(lista):
        print(f'{i + 1}, ', end='')

print(f'\nO menor valor é {min(lista)} e se encontra nas posições ', end='')

for i, v in enumerate(lista):
    if v == min(lista):
        print(f'{i + 1}, ', end='')
