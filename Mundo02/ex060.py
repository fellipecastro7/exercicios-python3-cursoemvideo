'''Exercício 060 - Cálculo do Fatorial
Faça um programa que leia um número qualquer e mostre o seu fatorial.'''

'''/// Usando WHILE ///'''
num = int(input('Insira um número: '))

fatorial = num - 1
resultado = num * fatorial
i = fatorial - 1

while i > 0:
    fatorial -= 1
    resultado *= fatorial
    i -= 1

print(f'{num}! é igual a {resultado}.')

'''/// Usando FOR ///'''
'''num = int(input('Insira um número: '))

fatorial = num - 1
resultado = num * fatorial

for i in range(fatorial - 1, 0, -1):
    fatorial -= 1
    resultado *= fatorial

print(f'{num}! é igual a {resultado}.')'''
