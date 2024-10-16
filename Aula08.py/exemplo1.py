x = 2

if x < 0:
    print('A')
elif x >= 1 and x <= 3:
    print('B')
elif x < 10:
    print('C')
else:
    print('D')

'''
A ordem dos if / elif / elif importa!
A primeira condição verdadeira é aquela que terá o bloco de código associado
executado.

Nesse caso, com x = 2, a primeira condição verdadeira é "x >= 1 and x <= 3".
Portanto, o programa irá printar a letra B.
'''