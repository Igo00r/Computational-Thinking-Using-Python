def exemplo():
    x = 5 #Essa é OUTRA variável, que só existe no escopo da função
 
def main():
    print("O programa está começando...")
    x = 3
    exemplo()
    print(x)
   


if __name__ == 'main':
    main()
    
    '''
    Todas as linhas que não estão dentro da função são executados
    (na ordem que estão escritas)
    '''