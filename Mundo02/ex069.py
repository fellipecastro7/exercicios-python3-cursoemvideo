'''Exercício 069 - Análise de dados do grupo
Crie um programa que leia a idade e o sexo de várias pessoas. A cada pessoa cadastrada, o programa
deverá perguntar se o usuário quer continuar ou não continuar. No final, mostre:

A) Quantas pessoas têm mais de 18 anos.
B) Quantos homens foram cadastrados.
C) Quantas mulheres têm menos de 20 anos.'''

print('=-' * 10)
print('CADASTRO DE PESSOAS')
print('=-' * 10)

mais18 = 0
homens = 0
mulheres = 0

while True:
    idade = int(input('Insira a idade: '))

    while idade <= 0:
        idade = int(input('Insira a idade: '))

    if idade > 18:
        mais18 += 1

    sexo = input('Insira o sexo [M / F]: ').strip().upper()

    while sexo not in 'MF':
        sexo = input('Insira o sexo [M / F]: ').strip().upper()

    if sexo == 'M':
        homens += 1

    elif sexo == 'F' and idade < 20:
        mulheres += 1

    print('Cadastro realizado com sucesso!\n')
    opcao = input('Deseja continuar o cadastro de pessoas? [S/ N] ').strip().upper()

    while opcao not in 'SN':
        opcao = input('Deseja continuar o cadastro de pessoas? [S/ N] ').strip().upper()

    if opcao == 'N':
        break

print(f'\n{mais18} pessoas têm mais de 18 anos.')
print(f'{homens} homens foram cadastrados.')
print(f'{mulheres} mulheres têm menos de 20 anos.')
