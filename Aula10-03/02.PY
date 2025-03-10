import json

NOME_ARQUIVO = 'outro_arquivo.json'

# lê arquivo JSON e retorna a lista de pacientes
def carrega_pacientes():
    try: # tente fazer o seguinte bloco de código:
        with open(NOME_ARQUIVO) as arquivo:
            pacientes = json.load(arquivo)
    except: # se alguma linha der erro, faça isso no lugar:
        pacientes = []
    finally: # não importa qual o caminho percorrido, no final faça isso:
        return pacientes

# recebe a lista de pacientes e escreve seus dados no arquivo JSON
def escreve_pacientes_no_arquivo(pacientes: list):
    # abro arquivo no modo de escrita (Write, por isso o w)
    with open(NOME_ARQUIVO, 'w') as arquivo:
        # parâmetros: dado a escrever; arquivo; espaçamento da indentação (opcional)
        json.dump(pacientes, arquivo, indent = 4)

# recebe lista de pacientes e exibe apenas os seus nomes
def mostra_nomes(pacientes: list):
    for paciente in pacientes:
        print(paciente['nome']) # acesso apenas campo "nome"

# pede dados de paciente por input e retorna o paciente criado
def le_novo_paciente():
    paciente = {} # dicionário começa vazio

    print('Informe o nome do paciente:')
    nome = input()
    paciente['nome'] = nome

    # Exercício: ler idade e ID interno, e colocar
    # nos respectivos campos do dicionário
    print('Informe idade do paciente:')
    idade = int(input())
    paciente['idade'] = idade

    print('Informe o ID interno do paciente:')
    ID = int(input())
    paciente['id'] = ID

    return paciente

'''
Exercício: escreva função que recebe lista de pacientes e
printa todas as informações (nome, idade, id)
'''
# recebe lista de pacientes e mostra todos os dados de cada um
def mostra_dados(pacientes: list):
    for paciente in pacientes:
        print('Nome:', paciente['nome'])
        print('Idade:', paciente['idade'])
        print('ID interno:', paciente['id'])
        print()

def main():
    pacientes = carrega_pacientes()
    print('Arquivo de dados carregado com sucesso.')
    em_execucao = True
    while em_execucao:
        print('Escolha uma opcao:')
        print('0. Sair do programa')
        print('1. Mostrar pacientes')
        print('2. Cadastrar paciente')

        opcao = int(input())
        if opcao == 0:
            em_execucao = False
        elif opcao == 1:
            mostra_dados(pacientes)
        elif opcao == 2:
            novo_paciente = le_novo_paciente()
            pacientes.append(novo_paciente)

    print('Programa vai terminar!')
    escreve_pacientes_no_arquivo(pacientes)
    print('Base de dados atualizada com sucesso.')
    print('Encerrando...')
    
main()