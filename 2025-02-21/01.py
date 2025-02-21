'''
Este programa lê um inteiro N e imprime todos os
números PARES de 0 até N.
'''

print('Digite um inteiro positivo.')
N = int(input())
'''
i = 0
while i <= N:
print(i)
i = i+2
'''

# equivalente às linhas comentadas acima:

for i in range(0, N+1, 2):
    print(i)