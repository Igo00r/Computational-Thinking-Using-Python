# Menu para cadastro de dados de doador de sangue

nome = 'Não consta'
tipo_sanguineo = 'Não consta'

continua_programa = True

while continua_programa:
    print('Escolha uma opção:')
    print('A - cadastrar nome')
    print('B - cadastrar tipo sanguíneo')
    print('C - ENCERRAR PROGRAMA')
    comando = input()
    if comando == 'A':
        print('Digite o nome:')
        nome = input()
    elif comando == 'B':
        print('Digite o tipo sanguíneo:')
        tipo_sanguineo = input()
    elif comando == 'C':
        continua_programa = False
        print('Encerrando menu...')
    else:
        print('Comando não reconhecido!')

print()
print('Informações do doador:')
print('Nome:', nome)
print('Tipo sanguíneo:', tipo_sanguineo)