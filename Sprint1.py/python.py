import os #Importar biblioteca para utilizar o comando "cls" 

maquinistas = [] #Duas listas globais para armazenar os valores emitidos
trens = []

def exibir_titulo():  #Função com objetivo de Mostrar o título
    print("𝑪𝑪𝑹 𝑹𝒂𝒊𝒍𝑺𝒚𝒏𝒄\n" )




def exibir_option(): #Função com objetivo de Mostrar as opções
    print("1. Cadastrar operadores ")
    print("2. Cadastrar trem ")
    print("3. Visualizar trens cadastrados ")
    print("4. Visualizar operadores cadastrados")
    print("5. Sair\n ")



def voltar_menu(): #Função de retornar ao menu
    print("Retornando ao menu") 
    main()

def option_invalida():  #Quando uma opção inválida eh escrita ele retorna ao menu
    print("Opção inválida! \n")
    input("Digite uma tecla para voltar: ")
    voltar_menu()



def exibir_subtitulo(texto): #Ao entrar nas funções das opções mostradas (1 ao 4) exibe um subtitulo que limpa o terminal e utiliza o parametro texto para facilitar em oque escrever em cada opção selecionada
    os.system("cls")
    print(texto)
    print()


def cadastrar_maquinista(): #Função para cadastrar os maqunistas desejados, utilizei tambem F string como boas práticas
    exibir_subtitulo("Cadastrar novo maquinista")
    nome_maquinista = input("Digite nome e sobrenome do operador: ") #criei uma váriavel que é adicionada a lista 
    print(f"O operador {nome_maquinista} foi cadastrado com sucesso!")
    maquinistas.append(nome_maquinista) #APPEND adiciona o nome ao final da lista 
    input("Digite qualquer tecla para retornar ao menu: ")
    voltar_menu()

def cadastrar_trem(): #Função para cadastrar os trens desejados, utilizei tambem F string como boas práticas
    exibir_subtitulo("Cadastrar novo trem")
    nome_trem = input("Digite número de série do trem: ") #criei uma váriavel que é adicionada a lista 
    trens.append(nome_trem)   #APPEND adiciona o nome ao final da lista 
    print(f"O trem {nome_trem} foi cadastrado com sucesso!")
    input("Digite qualquer tecla para retornar ao menu: ")
    voltar_menu()

def mostrar_maquinista(): # Função igual ao de mostrar trens
    exibir_subtitulo("Maquinistas cadastrados")
    if len(maquinistas) == 0:
        print("Não há nennhum maquinista cadastrado!")
    else:
        for maquinista in maquinistas:
            print(maquinista)
    input("\nPressione qualquer tecla para voltar ao menu ")
    voltar_menu()

def mostrar_trem(): #Função da opção 3 que mostra os trens cadastrados 
    exibir_subtitulo("Trens cadastrados")
    if len(trens) == 0: #Se a quantidade de trens cadastrados forem 0, retorna a mensagem a baixo
        print("Não há nennhum trem cadastrado!")
    else:
        for trem in trens: # Se não, ele mostra a váriavel trem dentro de "trens" (lista) e da print na quantidade de trens
            print(trem)
    input("\nPressione qualquer tecla para voltar ao menu ")
    voltar_menu()

def escolher_option(): #Função com o objetivo de escolher a opção
    try:    #Utilizei o comando TRY EXCEPT para quando o usuário digitar algo inexiste no programa. Por exemplo: se o usuário digitar uma String, ele cai como opção inválida
        option = int(input("Selecione sua opção: "))
        if option == 1:
            cadastrar_maquinista()
        elif option == 2:
            cadastrar_trem()
        elif option == 3:
            mostrar_trem()
        elif option == 4:
            mostrar_maquinista()
        elif option == 5:
            sair()
        else:  #Caso o usário digite um INT ele retorna direto para opção inválida
            option_invalida()
    except:
        option_invalida() #Se ele digitar uma STRING ele retorna para a função de opção inválida.





   
def sair():
    os.system('cls') #Comando CLS serve para limpar o terminal
    print("Programa está sendo encerrado!")





def main(): #Main signfica a função principal do meu programa, então toda vez que main for chamada, vai executar as funções de Mostrar o nome do APP, mostrar as opções e escolher as opções 
    os.system("cls")
    exibir_titulo()
    exibir_option()
    escolher_option()
    
    



if __name__ == "__main__": #Obrigatório para que funcione a função Main
    main()

