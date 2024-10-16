'''
Algumas formas de modificar conteúdo da lista:

* Substituir elementos
* Adicionar elementos
* Remover elementos
'''

# (1) Modificação (substituição)
compras = ['alface', 'banana', 'iogurte']
print('Lista original:')
print(compras)

print()

compras[0] = 'rúcula'   # coloco rúcula no lugar de alface
compras[1] = 'melancia' # coloco melancia no lugar de banana
print('Lista modificada:')
print(compras)

print()

# (2) Adicionar elementos
compras.append('escova de dente') # adiciona no final da lista
print('Após adicionar elemento:')
print(compras)

print()

# também existem o extend e o insert


# (3) Remover elementos
compras.remove('iogurte') # busca o valor na lista; se encontrar, remove
print('Após remover iogurte:')
print(compras)

compras.remove('queijo')