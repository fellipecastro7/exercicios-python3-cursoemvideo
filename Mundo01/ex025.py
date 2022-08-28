'''Exercício 025 - Procurando uma string dentro de outra
Crie um programa que leia o nome de uma pessoa e diga se ela tem "SILVA" no nome.'''

nome = input('Informe o seu nome completo: ').strip()

nome1 = 'SILVA' in nome.upper()

print(f'\nSeu nome é {nome}')
print(f'Contém "SILVA"? {nome1}')
