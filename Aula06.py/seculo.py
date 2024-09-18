print('Qual o século?')

sec = int (input())

ano_final = sec*100
ano_inicial = ano_final - 99

print('Este século vai do ano', ano_inicial , 'até o ano' , ano_final)

if sec == 21:
    print('Este é o século atual.')
else:
    print('Este NÃO é o século atual.')
    