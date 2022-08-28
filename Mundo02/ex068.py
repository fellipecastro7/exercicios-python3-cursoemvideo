'''Exercício 068 - Jogo do Par ou Ímpar
Faça um programa que jogue par ou ímpar com o computador. O jogo só será interrompido quando o
jogador PERDER, mostrando o total de vitórias consecutivas que ele conquistou no final do jogo.'''

from random import randint

print('=-' * 7)
print('PAR OU ÍMPAR')
print('-=' * 7)

vitorias = 0

while True:
    computador = randint(0, 10)
    usuario = int(input('Insira um número para jogar: '))
    jogada = input('Escolha sua jogada [P / I]: ').strip().upper()

    while jogada not in 'PI':
        jogada = input('Escolha sua jogada [P / I]: ').strip().upper()

    resultado = computador + usuario
    print(f'\nVocê jogou {usuario} e o computador {computador}.')
    print(f'{usuario} + {computador} = {resultado}')

    if jogada == 'P':
        if resultado % 2 == 0:
            print('Você venceu.\n')
            vitorias += 1

        else:
            print('Você perdeu.\n')
            break

    else:
        if resultado % 2 != 0:
            print('Você venceu.\n')
            vitorias += 1

        else:
            print('Você perdeu.\n')
            break

print(f'Você venceu {vitorias} vezes.')
