 # Menu para cadastro de dados de doador de sangue

nome = 'Não consta'
tipo sanguíneo = 'Não consta'

while True:
 print('Escolha uma opção:')
 print('A - cadastrar nome')
 print('B - cadastrar tipo sanguíneo')
 print('C - ENCERRAR PROGRAMA')

 comando =  input()
 if comando == 'A':
    print('Digite o nome:')
    nome = input()

elif comando == 'B':
    print = ('Digite o tipo snaguíneo:')
    tipo_sanguineo = input()

elif comando == 'C':
    continua_programa = False
    print('Encerrando meu...')

else:
    print('Comando não reconhecido!')

print('Informações do doador:')
print('')