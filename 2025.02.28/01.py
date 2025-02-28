# lista = []
# for VARIAVEL in SEQUENCIA:
#     if CONDICAO:
#         lista.append(EXPRESSAO)

# (o if é opcional, para caso queiramos algum filtro)

# lista = [ EXPRESSAO for VARIAVEL in SEQUENCIA if CONDICAO ]

# EXEMPLO
valores = [ 3, 10, -6, 8, 47, 0, 5, 11, 9 ]
menores_que_10 = [ valor for valor in valores if valor < 10 ]

'''
EXERCÍCIO: transformar a linha 12 (logo acima) em bloco de código
com for e append explícitos.
'''
menores_que_10 = []
for valor in valores:
    if valor < 10:
        menores_que_10.append(valor)