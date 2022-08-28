'''Exercício 054 - Grupo da Maioridade
Crie um programa que leia o ano de nascimento de sete pessoas. No final, mostre quantas pessoas
ainda não atingiram a maioridade e quantas já são maiores.'''

from datetime import date
atual = date.today().year
menor = 0
maior = 0

for i in range(7):
    ano = int(input('Informe o ano de nascimento: '))
    idade = atual - ano
    if idade < 21:
        menor += 1
    else:
        maior += 1
print(f'{menor} pessoas ainda não atingiram a maioridade.')
print(f'{maior} pessoas já são de maiores.')
