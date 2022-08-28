'''Exercício 073 - Tuplas com Times de Futebol
Crie uma tupla com os 20 primeiros colocados da tabela do Campeonato Brasileiro de Futebol, na ordem
de colocação. Depois mostre:

A) Os 5 primeiros.
B) Os últimos 4 colocados.
C) Times em ordem alfabética.
D) Em que posição está o time do Ceará SC.'''

times = ('Palmeiras', 'Corinthians', 'Internacional', 'Athletico-PR', 'Atlético-MG', 'Fluminense',
'Flamengo', 'São Paulo', 'Santos', 'Botafogo', 'Avaí', 'Bragantino', 'Goiás', 'Ceará SC', 'Cuiabá',
'Coritiba', 'América-MG', 'Atlético-GO', 'Juventude', 'Fortaleza')

print(f'Os 5 primeiros colocados são: {times[:5]}')
print('=-' * 20)
print(f'Os 4 últimos colocados são: {times[16:]}')
print('=-' * 20)
print(f'Times em ordem alfabética: {sorted(times)}')
print('=-' * 20)
print(f'O time do Ceará SC se encontra na {times.index("Ceará SC") + 1}º posição.')
