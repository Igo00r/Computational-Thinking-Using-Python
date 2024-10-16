print('Escolhq uma opção de 1 a 3:')
opcao = int (input())

contagem_tentativas = 1

while (opcao < 1 or opcao > 3) and contagem_tentativas < 5:
    print('Opção inválida. Por favor escolha uma opção de 1 a 3:')
    opcao = int(input())
    contagem_tentativas += 1 # aumenta em 1 unidade a contagem de tentativas

if contagem_tentativas == 5:
    print('Sinto muito, não entendi suas instruções.')
else:
    print('Entendendido! A opção escolhida foi', opcao)
