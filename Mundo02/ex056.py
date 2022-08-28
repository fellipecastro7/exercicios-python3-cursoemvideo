'''Exercício 056 - Analisador completo
Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas. No final do programa, mostre:

- A média de idade do grupo.
- Qual é o nome do homem mais velho.
- Quantas mulheres têm menos de 20 anos.'''

pessoas = {}
media = 0
maior = 0
menos20 = 0

for i in range(4):
    nome = input('Informe seu nome: ').strip()
    idade = int(input('Informe a sua idade: '))
    if idade > 0:
        media += idade
    else:
        print('Erro! Informe uma idade válida.')
        break
    sexo = input('Informe seu sexo (M ou F): ').strip().upper()
    print()
    if sexo in ('M', 'MASCULINO'):
        pessoas[nome] = idade
        if idade > maior:
            maior = idade
    elif sexo in ('F', 'FEMININO'):
        if idade < 20:
            menos20 += 1
    else:
        print('Erro! Entre com "M" ou "F".')
        break
print(f'A média de idade do grupo é de {media / 4:.1f} anos.')
print(f'O homem mais velho tem {maior} anos e se chama {max(pessoas, key=pessoas.get)}.')

if menos20 == 0:
    print('Nenhuma mulher tem menos de 20 anos.')
elif menos20 == 1:
    print('1 mulher tem menos de 20 anos.')
else:
    print(f'{menos20} mulheres têm menos de 20 anos.')
