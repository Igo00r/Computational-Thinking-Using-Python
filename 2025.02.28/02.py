def primo(n):
    if n <= 1:
        return False
    if n == 2:
        return True
    if n % 2 == 0: # se não é 2 mas é par, então não é primo
        return False
    
    # vou testar apenas divisores ímpares! Já testei se o número é par.
    for possivel_divisor in range(3, n, 2):
        if n % possivel_divisor == 0:
            # encontrei divisor de n. Então n não é primo
            return False
    return True

numeros_primos = []
for n in range(1000, 1200):
    if primo(n):
        numeros_primos.append(n)

'''
Exercício: usar compreensão de lista para encurtar o bloco de código
acima (linhas 16 a 19).
'''

numeros_primos = [ n for n in range(1000, 1200) if primo(n) ]
print(numeros_primos)