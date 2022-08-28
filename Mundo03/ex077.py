'''Exercício 077 - Contando vogais em Tupla
Crie um programa que tenha uma tupla com várias palavras (não usar acentos). Depois disso, você deve
mostrar, para cada palavra, quais são as suas vogais.'''

palavras = ('APRENDER', 'PROGRAMAR', 'LINGUAGEM', 'PYTHON', 'CURSO', 'GRATIS', 'ESTUDAR', 'PRATICAR',
            'TRABALHAR', 'MERCADO', 'PROGRAMADOR', 'FUTURO')

for i in palavras:
    print(f'\nNa palavra {i}, temos as vogais ', end='')

    for j in i:
        if j.upper() in 'AEIOU':
            print(f'{j}', end=' ')
