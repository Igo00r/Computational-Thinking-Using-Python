compras = []

print('Vamos crias a sua lista de compras!')
print('Quantos itens ela vai ter?')
n = int(input())

for i in range(n):
    # ler por input um item e salvar na lista de compras usando append

    item = input(f'Insira o item {i + 1}: ')  # Lê o nome do item
    compras.append(item)  # Adiciona o item à lista

print('Sua lista de compras:', compras)