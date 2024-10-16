print('Escolhq uma opção de 1 a 3:')
opcao = int (input())

while opcao < 1 or opcao > 3:
    print('Opção inválida. Por favor escolha uma opção de 1 a 3:')
    opcao = int(input())

print('A opção escolhida foi', opcao)