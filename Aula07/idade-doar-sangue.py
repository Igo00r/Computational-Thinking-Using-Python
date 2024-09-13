print('Em que ano você nasceu?')
ano_nascimento = int(input())

idade = 2024 - ano_nascimento

# critério de idade para doar sangue: 16 a 69 anos

if idade >= 18 and idade <= 69:
    print('já tá podendo tirar')
elif idade == 16 or idade == 17:
    print('está quase lá,','você precisa de autorização dos papais!')
else:
    print('pode não bbzinho')
    