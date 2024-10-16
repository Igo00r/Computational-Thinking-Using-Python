'''
string e lista oferecem vários métodos (operações) que fornecem
utilidades para trabalhar com os dados
'''

# len captura o número de elementos na sequência
# (len = length = comprimento)
x = 'bom dia!'
print('A mensagem', x, 'possui tamanho', len(x))

compras = ['alface', 'banana', 'iogurte']
print('A lista de compras contém', len(compras), 'itens')

intervalo = range(10) # intervalo de 0 até 9
print('O intervalo range(10) tem tamanho', len(intervalo))

print('\n')

# Acesso de elemento específico via índice
compras = ['alface', 'banana', 'iogurte']
print(compras[0]) # acessa elemento no índice zero, ou seja, primeiro da lista

# (no caso da lista, podemos inclusive modificar o elemento)
compras[0] = 'rúcula'
print(compras)

nome = 'samuel'
print(nome[2])