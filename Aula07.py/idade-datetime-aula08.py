import datetime

data = datetime.datetime.now() # data de AGORA, incluiondo ano, mês, .... até milissegundos
ano_atual = data.year # pego apenas o cmapo YEAR (ano) da data atual

print('Em que ano você nasceu?')
ano_nascimento = int(input())

idade = ano_atual - ano_nascimento

print('Estamos no ano', ano_atual)
print('Portanto você fez ou fará', idade , 'anos neste ano')

print("Em que mês você nasceu?")
mês_aniversário = int(input())


print('Em que dia você nasceu?')
dia_aniversário = int(input())


mês_atual = data.month
dia_atual = data.day

if mês_aniversário < mês_atual: 
    print('Você já fez aniversário esse ano')
elif mês_aniversário == mês_atual and dia_aniversário <= dia_atual:
    print('Você já fez aniversário esse ano')
else:
    print('Você ainda não fez aniversário esse ano')
    
    

'''
Exercício para sexta-feira:

* Pegar os campos "month" e "day" da data atual
* Perguntar o dia e mês de nascimento do usuário
* Descobrir se a pessoa já fez aniversário esse ano e printar uma mensagem de acordo
'''