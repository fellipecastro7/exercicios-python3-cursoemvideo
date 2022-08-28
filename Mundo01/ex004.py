''' Exercício 004 - Dissecando uma Variável
Faça um programa que leia algo pelo teclado e mostre na tela o seu tipo primitivo e todas as
informações possíveis sobre ela.'''

a = input('Digite algo: ')
print('\nO tipo primitivo desse valor é ', type(a))
print('É um número? ', a.isnumeric())
print('É alfabético? ', a.isalpha())
print('É alfanumérico? ', a.isalnum())
print('Só tem letras maiúsculas? ', a.isupper())
print('Só tem espaços? ', a.isspace())
print('Só tem letras minúsculas? ', a.islower())
print('Está capitalizada? ', a.istitle())
