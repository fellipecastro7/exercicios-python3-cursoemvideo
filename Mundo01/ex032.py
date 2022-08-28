'''Exercícios 032 - Ano bissexto
Faça um programa que leia um ano qualquer e mostre se ele é BISSEXTO.'''

from datetime import date
ano = int(input('Informe um ano (DIGITE 0 PARA SELECIONAR O ANO ATUAL): '))

if ano == 0:
    ano = date.today().year
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print(f'\n{ano} É UM ANO BISSEXTO!')
else:
    print(f'\n{ano} NÃO É UM ANO BISSEXTO!')
