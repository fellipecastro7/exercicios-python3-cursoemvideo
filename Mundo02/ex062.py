'''Exercício 062 - Super Progressão Aritmética v3.0
Melhore o DESAFIO 061, perguntando para o usuário se ele quer mostrar mais alguns termos. O programa
encerra quando ele disser que quer mostrar 0 termos.'''

print('=-=-=- PROGRESSÃO ARITMÉTICA -=-=-=')
a1 = int(input('Insira o 1° termo da PA: '))
razao = int(input('Insira a razão da PA: '))
print(a1, end='  ')

flag = False
a10 = a1 + (10 - 1) * razao
i = a1 + razao

while i < a10 + razao or i > a10 + razao:
    print(i, end='  ')
    i += razao

ai = a10 + razao

while flag is False:
    termos = int(input('\nDeseja ver mais quantos termos? '))
    c = 0

    if termos != 0:
        while c < termos:
            print(ai, end='  ')
            ai += razao
            c += 1

    else:
        flag = True
