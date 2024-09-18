import datetime

data = date.time.now() # data de AGORA, incluiondo ano, mês, .... até milissegundos
ano_atual = data.year # pego apenas o cmapo YEAR (ano) da data atual

print('Em que ano você nasceu?')
ano_nascimento = int(input())

idade = ano_atual - ano_nascimento

print('Estamos nos ano', ano_atual)
print('Portanto você fes ou fará', idade, 'anos neste ano')

'''
Exercício para sexta-feira:

* Pegar os campos "month" e "day" da data atual
* Perguntar o dia e mês de nascimento do usuário
* Descobrir se a pessoa já fez aniversário esse ano e printar uma mensagem de acordo
'''