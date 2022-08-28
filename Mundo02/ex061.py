'''Exercício 061 - Progressão Aritmética v2.0
Refaça o DESAFIO 051, lendo o primeiro termo e a razão de uma PA, mostrando os 10 primeiros termos
da progressão usando a estrutura while.'''

a1 = int(input('Insira o 1° termo da PA: '))
razao = int(input('Insira a razão da PA: '))
print(a1, end='  ')

a10 = a1 + (10 - 1) * razao
i = a1 + razao

while i < a10 + razao or i > a10 + razao:
    print(i, end='  ')
    i += razao
