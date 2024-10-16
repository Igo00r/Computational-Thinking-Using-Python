'''
Sequências de dados também permitem testar existência de elemento na sequência

sintaxe:
VALOR in SEQUÊNCIA

essa expressão tem valor True se o VALOR existe na SEQUÊNCIA.
'''

compras = ['alface', 'banana', 'iogurte']
if 'banana' in compras:
    print('Preciso comprar banana')

if 'manga' not in compras:
    print('Não preciso comprar manga')

mensagem = 'estamos chegando ao final da aula...'
if 'a' in mensagem:
    print('A mensagem contém letra a')

if 'oi' in mensagem:
    print('A mensagem contém oi')
else:
    print('A mensagem não contém oi')

if 'final' in mensagem:
    print('A mensagem contém a palavra final')

if 3 in range(2, 7):
    print('O intervalo de 2 até 6 contém o número 3')