'''Exercício 058 - Jogo da Adivinhação v2.0
Melhore o jogo do DESAFIO 028, onde o computador vai "pensar" em um número entre 0 e 10. Só que
agora o jogador vai tentar adivinhar até acertar, mostrando no final quantos palpites foram
necessários para vencer.'''

from random import randint
from time import sleep

num_comp = randint(0, 10)
tentativas = 0
flag = False

print('\033[33m-=' * 10)
print('\033[33mJOGO DA ADIVINHAÇÃO')
print('\033[33m-=\033[m' * 10)

while not flag:
    num_user = int(input('Tente adivinhar o número escolhido pelo computador (ENTRE 0 E 10): '))
    tentativas += 1
    print('\033[34mPROCESSANDO...\033[m')
    sleep(2)

    if num_user == num_comp:
        flag = True

    else:
        print('Você errou.')

print(f'\033[35mO número escolhido pelo computador foi {num_comp}.\033[m')
print('\033[1;32mPARABÉNS, VOCÊ ACERTOU!\033[m')
print(f'Você precisou de {tentativas} tentativas para acertar.')
