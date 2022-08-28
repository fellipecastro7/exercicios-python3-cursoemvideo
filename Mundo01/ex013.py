'''Exercício 013 - Reajuste Salarial
Faça um programa que leia o salário de um funcionário e mostre seu novo salário, com 15% de
aumento.'''

salario = float(input('Digite seu salário: R$'))

aumento = salario * (15 / 100)

novo_salario = salario + aumento
print(f'\nO seu novo salário com 15% de aumento é de: R${novo_salario:.2f}')
