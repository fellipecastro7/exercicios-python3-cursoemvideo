'''Exercício 028 - Jogo da adivinhação v.1.0
Escreva um programa que faça o computador "pensar" em um número inteiro entre 0 e 5 e peça para o
usuário tentar descobrir qual foi o número escolhido pelo computador.
O programa deverá escrever na tela se o usuário venceu ou perdeu.'''

from random import randint
from time import sleep
print('\033[33m-=' * 10)
print('\033[33mJOGO DA ADIVINHAÇÃO')
print('\033[33m-=\033[m' * 10)

num_comp = randint(0, 5)

num_user = int(input('\033[1mTente adivinhar o número escolhido pelo computador (ENTRE 0 E 5): \033[33m'))
print('\033[34mPROCESSANDO...\033[m')
sleep(2)
print(f'\033[35mO número escolhido pelo computador foi {num_comp}.\033[m')
if num_user == num_comp:
    print('\033[1;32mPARABÉNS, VOCÊ VENCEU!\033[m')
else:
    print('\033[1;31mVOCÊ PERDEU!\033[m')
