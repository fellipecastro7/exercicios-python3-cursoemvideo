'''Exercício 041 - Classificando Atletas
A Confederação Nacional de Natação precisa de um programa que leia o ano de nascimento de um atleta
e mostre sua categoria, de acordo com a idade:

- Até 9 anos: MIRIM
- Até 14 anos: INFANTIL
- Até 19 anos: JUNIOR
- Até 20 anos: SÊNIOR
- Acima: MASTER'''

from datetime import date
ano = int(input('Informe seu ano de nascimento: '))

atual = date.today().year
idade = atual - ano

print(f'\nVocê tem {idade} anos em {atual}.')

if idade <= 9:
    print('Categoria: MIRIM')
elif idade <= 14:
    print('Categoria: INFANTIL')
elif idade <= 19:
    print('Categoria: JUNIOR')
elif idade <= 20:
    print('Categoria: SÊNIOR')
else:
    print('Categoria: MASTER')
