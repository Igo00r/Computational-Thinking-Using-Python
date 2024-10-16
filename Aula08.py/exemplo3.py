print('Escolha um valor inicial para x:')
x = int(input())

while x < 10: # "enquanto x for menor que 10, execute o bloco de código a seguir:"
    print('A')
    print('Estou dentro do while porque x vale', x)
    x = x + 1

print('fim do programa! x =', x)