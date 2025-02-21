'''
Recebe u número n e devolve True, se é número primo; False caso cotrário

Um número n é primoe é divisível APENAS por 
'''

def primo(n):
    for possivel_divisor in range(2, n):
        if n % possivel_divisor == 0:
            # econtrei divisor de n! Então n não é primo 
            return False
    return True    

'''
Exercício: faça um programa que printa, dentre os números de
1 até 10, apenas aquele que são primos
'''
for numero in range(1, 99999999999999999999999999999999999999999999999999999):
    if primo(numero):
        print(f'{numero} é primo')