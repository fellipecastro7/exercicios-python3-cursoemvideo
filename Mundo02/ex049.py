'''Exercício 049 - Tabuada v.2.0
Refaça o desafio 009, mostrando a tabuada de um número que o usuário, só que agora utilizando um
laço for.'''

num = int(input('Informe um número: '))
print('=-=-=-=- TABUADA -=-=-=-=')

for i in range(11):
    print(f'{num} x {i:^2} = {num * i:}')
