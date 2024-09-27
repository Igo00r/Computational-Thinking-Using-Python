idade = int(input("Digite sua idade:\n"))
renda_mensal = float(input("Digite sua renda mensal:\n"))

if 21 <= idade <= 55 and renda_mensal >= 3000:
    print('Parabéns! Você recebeu o cartão especial!')
else:
    print('Sinto muito, no momento o cartão está indisponível.')