texto1 = 'bom dia'


for caractere in texto1:
    print (caractere)

texto2 = 'bom dia, estamos na aula de computational thinking!'
print(texto2)
a = 0
for caractere in texto2:
    if caractere == ' ':
        a += 1
print('O texto2 tem', a,'a')

#modifique esse código para contar quantas letras "a"

contador = 0
for caractere in texto2:
    if caractere == ' ':
        contador += 1

n = 5  # Exemplo de valor para n
multiplo = 3  # Exemplo de valor para multiplo

print(n, 'x', multiplo, '=', n * multiplo)


print('\n------------------------------/n')