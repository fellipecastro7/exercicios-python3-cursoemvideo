'''Exercício 027 - Primeiro e último nome de uma pessoa
Faça um programa que leia o nome completo de uma pessoa, mostrando em seguida o primeiro e o último
nome separadamente.'''

nome = input('Digite o seu nome completo: ').strip()

nomeM = nome.split()

print(f'\nO seu nome completo é: {nome}')
print(f'O seu primeiro nome é: {nomeM[0]}')
print(f'O seu último nome é: {nomeM[len(nomeM) - 1]}')
