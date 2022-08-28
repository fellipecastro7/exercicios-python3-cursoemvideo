'''Exercício 075 - Análise de Dados em uma Tupla
Desenvolva um programa que leia quatro valores pelo teclado e guarde-os em uma tupla. No final,
mostre:

A) Quantas vezes apareceu o valor 9.
B) Em que posição foi digitado o primeiro valor 3.
C) Quais foram os números pares.'''

num = (int(input('Insira um número: ')), int(input('Insira mais um número: ')),
        int(input('Insira mais um número: ')), int(input('Insira mais um número: ')))

print('Os valores inseridos foram: ', end='')

for i in num:
    print(f'{i}', end='  ')

print(f'\nO número 9 apareceu {num.count(9)} vez(es).')

if 3 in num:
    print(f'O número 3 foi inserido, pela 1º vez, na {num.index(3) + 1}º posição.')

else:
    print('O número 3 não foi inserido nenhuma vez.')

print('Os valores pares inseridos foram: ', end='')

for i in num:
    if i % 2 == 0:
        print(f'{i}', end='  ')
