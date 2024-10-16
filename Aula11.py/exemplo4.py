'''
Utilidades específicas da classe str (string)
'''

mensagem = '  Esta mensagem contém várias coisas. Vamos usar como exemplo! '
print(mensagem)

mensagem = mensagem.strip() # remove espaços sobrando no início e fim da string
print(mensagem)

print('Deseja continuar? (S/N)')
resposta = input()
resposta = resposta.lower() # passa a resposta para letras minúsculas
if resposta == 's':
    print('Ok, continuando!')
elif resposta == 'n':
    print('Ok, parando...')
    exit() # termina programa imediatamente
else:
    print('Não entendi a resposta, mas vou continuar então...')

print(mensagem.upper()) # mostra a mensagem toda com letras maiúsculas
print(mensagem)

print('Fim.')
