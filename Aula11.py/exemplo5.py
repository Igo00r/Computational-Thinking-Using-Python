'''
Algumas utilidades da classe list (lista)
'''

compras = ['alface', 'banana', 'iogurte']
print('Lista original:')
print(compras)

print()

compras[0] = 'rúcula'
compras[1] = 'melancia'
print('Lista modificada:')
print(compras)

print()

compras.sort() # ordena a lista
print('Lista modificada, agora em ordem crescente:')
print(compras)

print('\n---\n')

temperaturas = [ 19.1, 20.5, 21.3, 21.9, 23.0, 22.8, 19.0, 17.2]
menor_temp = min(temperaturas)
maior_temp = max(temperaturas)

print('Temperaturas:', temperaturas)
print('A máxima nesse dia foi', maior_temp)
print('A mínima nesse dia foi', menor_temp)