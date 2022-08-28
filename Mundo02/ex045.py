'''Exercício 045 - GAME: Pedra, Papel e Tesoura
Crie um programa que faça o computador jogar Jokenpô com você.'''

from random import choice
from time import sleep
print('\033[34m\t=-=-=-=-JOKENPÔ-=-=-=-=\033[m')
sleep(2)
print('\033[33mComputador: "Já decidi a minha jogada"\033[m')
escolha_user = input('Informe a sua jogada (Pedra, Papel ou Tesoura): ').strip().upper()
print('\n\033[35mPROCESSANDO...\033[m\n')
sleep(2)

lista = ['PEDRA', 'PAPEL', 'TESOURA']
escolha_comp = choice(lista)

if escolha_user == 'PEDRA' and escolha_comp == 'PEDRA':
    print(f'\033[33mComputador: "Eu escolhi {escolha_comp}!"\033[m')
    print('\033[36mEMPATE!\033[m')
elif escolha_user == 'PEDRA' and escolha_comp == 'PAPEL':
    print(f'\033[33mComputador: "Eu escolhi {escolha_comp}!"\033[m')
    print('\033[31mVOCÊ PERDEU!\033[m')
elif escolha_user == 'PEDRA' and escolha_comp == 'TESOURA':
    print(f'\033[33mComputador: "Eu escolhi {escolha_comp}!"\033[m')
    print('\033[32mVOCÊ VENCEU!\033[m')
elif escolha_user == 'PAPEL' and escolha_comp == 'PEDRA':
    print(f'\033[33mComputador: "Eu escolhi {escolha_comp}!"\033[m')
    print('\033[32mVOCÊ VENCEU!\033[m')
elif escolha_user == 'PAPEL' and escolha_comp == 'PAPEL':
    print(f'\033[33mComputador: Eu escolhi {escolha_comp}!"\033[m')
    print('\033[36mEMPATE!\033[m')
elif escolha_user == 'PAPEL' and escolha_comp == 'TESOURA':
    print(f'\033[33mComputador: "Eu escolhi {escolha_comp}!"\033[m')
    print('\033[31mVOCÊ PERDEU!\033[m')
elif escolha_user == 'TESOURA' and escolha_comp == 'PEDRA':
    print(f'\033[33mComputador: "Eu escolhi {escolha_comp}!"\033[m')
    print('\033[31mVOCÊ PERDEU!\033[m')
elif escolha_user == 'TESOURA' and escolha_comp == 'PAPEL':
    print(f'\033[33mComputador: "Eu escolhi {escolha_comp}!"\033[m')
    print('\033[32mVOCÊ VENCEU!\033[m')
elif escolha_user == 'TESOURA' and escolha_comp == 'TESOURA':
    print(f'\033[33mComputador: "Eu escolhi {escolha_comp}!"\033[m')
    print('\033[36mEMPATE!\033[m')
else:
    print('ERRO! JOGADA INVÁLIDA!')
