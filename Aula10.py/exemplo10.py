print('Qual a tabuada desejada?')
n = int(input())
for multiplo in range(10):
    print(n, 'x', multiplo, '=', n*multiplo)

# For faz a condição (multiplo < 10) e a atualização (multiplo +=10)