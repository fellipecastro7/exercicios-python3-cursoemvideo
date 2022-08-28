'''Exercício 022 - Analisador de Textos
Crie um programa que leia o nome completo de uma pessoa e mostre:
-> O nome com todas as letras maiúsculas e minúsculas.
-> Quantas letras ao todo (sem considerar espaços).
-> Quantas letras têm o primeiro nome.'''

nome = input('Informe seu nome completo: ').strip()

nomeM = nome.replace(' ', '')
nomeQ = nome.split()

print(f'\nSeu nome completo (COM TODAS AS LETRAS MAIÚSCULAS): {nome.upper()}')
print(f'Seu nome completo (COM TODAS AS LETRAS MINÚSCULAS): {nome.lower()}')
print(f'Seu nome tem {len(nomeM)} caracteres, sem considerar os espaços.')
print(f'O seu primeiro nome tem {len(nomeQ[0])} caracteres.')
