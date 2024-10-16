'''
Estrutura básica do for:

for VARIAVEL in SEQUENCIA:
    <alguma tarefa>

VARIAVEL é criada pelo for, caso não exista anteriormente

SEQUENCIA é qualquer sequência de dados em Python, como:
    - range
    - string
    - lista
'''

# range é sequência de inteiros em um intervalo
for i in range(5):
    print(i)

print('Valor final do i:', i) # valor do i aqui nessa linha?

print('---')

mensagem = 'bom dia!'
for c in mensagem: # passa por todos os caracteres da string mensagem
    print(c)

print('---')

compras = ['alface', 'banana', 'iogurte']
for item in compras:
    print(item)
