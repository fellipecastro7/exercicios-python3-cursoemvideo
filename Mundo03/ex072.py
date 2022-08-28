'''Exercício 072 - Número por Extenso
Crie um programa que tenha uma tupla totalmente preenchida com uma contagem por extenso, de zero até
vinte.

Seu programa deverá ler um número pelo teclado (entre 0 e 20) e mostrá-lo por extenso.'''

num = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez',
'onze', 'doze', 'treze', 'quatorze', 'quinze', 'dezesseis', 'dezesete', 'dezoito', 'dezenove',
'vinte')

opcao = int(input('Insira um número (entre 0 e 20): '))

while opcao < 0 or opcao > 20:
    opcao = int(input('Número inserido está fora do intervalo.\nInsira um número (entre 0 e 20): '))

print(f'Você digitou o número {num[opcao]}.')
