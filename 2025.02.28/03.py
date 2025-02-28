temperaturas = []
with open('dados.txt') as arquivo:
    for linha in arquivo:
        temperaturas.append(float(linha))

'''
Exercício: crie (usando compreensão de lista):
    (a) temperaturas_altas, contendo as temperaturas acima de 90

    (b) temperaturas_muito_altas, contendo as temperaturas acima de 100

Depois vamos ver o tamanho dessas listas comparadas com a lista total
de temperaturas, para ver qual proporção do tempo está em temperatura alta
'''