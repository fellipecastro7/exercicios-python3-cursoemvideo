'''Exercício 039 - Alistamento Militar
Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com sua idade:

- Se ele ainda vai se alistar ao serviço militar.
- Se é a hora de se alistar.
- Se já passou do tempo de alistamento.

Seu programa também deverá mostrar o tempo que falta ou que passou do prazo.'''

from datetime import date
ano = int(input('Informe o ano que você nasceu: '))

atual = date.today().year
idade = atual - ano

print(f'\nVocê tem {idade} anos em {atual}.')

if idade < 18:
    tempo = 18 - idade
    print('Você ainda irá se alistar ao serviço militar.')
    print(f'Faltam {tempo} anos para você se alistar.')
elif idade == 18:
    print('É a hora de se alistar.')
else:
    tempo = idade - 18
    print('Já passou do tempo de alistamento.')
    print(f'Já se passaram {tempo} anos do seu alistamento.')
