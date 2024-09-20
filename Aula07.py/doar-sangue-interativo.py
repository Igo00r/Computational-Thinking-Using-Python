print('Qual sua idade?')
idade = int(input())

if idade == 16 or idade == 17:
    print('Você tem autorização dos pais? (S/N)')
    resposta = input()
    if resposta == 's' or resposta == 'S':
        print('Pode doar sangue.')
elif idade >= 18: # simplificação
        print('Pode doar sangue.')
        resposta = input()
    
        