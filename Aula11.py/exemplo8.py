frutas = ['banana', 'maçã', 'uva', 'pera', 'manga']
legumes = ['abóbora', 'berinjela', 'chuchu']

compras = [] # carrinho de compras do usuário
print('Escolha uma fruta. As opções são:')
print(*frutas) # o asterisco serve para mostrar só o conteúdo sem os colchetes etc

fruta_escolhida = input()

# se a fruta escolhida é uma das opções disponibilizadas, adicionamos ao carrinho
if fruta_escolhida in frutas:
    compras.append(fruta_escolhida)
    print(fruta_escolhida, 'adicionada ao carrinho de compras.')
else:
    print(fruta_escolhida, 'indisponível; não adicionei nada ao carrinho de compras.')

'''
Exercício:

* faça o mesmo com os legumes: apresente as opções e peça para o usuário escolher
uma delas, adicionando ao carrinho (lista compras) se disponível;

* crie uma terceira categoria de compras, e faça da mesma forma.
(você irá criar uma lista de opções disponíveis e pedir que o usuário escolha alguma delas)

Ao final, printar pro usuário como ficou o carrinho de compras.

'''
