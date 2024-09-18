# Operador checa se  o elemento está contido em outro,
# o exemplo: "p" o "python" 
"p" in "python"
"yt" in "python"

x1 = 1
x2 = 2
x3 = 0.5
x4 = 0.25

n = 4

H = n/ (1 / x1 + 1 / x2 + 1 / x3 + 1 / x4)

x1_inv = 1 / x1
x2_inv = 1 / x2
x3_inv = 1 / x3
x4_inv = 1 / x4

denominador = x1_inv + x2_inv + x3_inv + x4_inv
H = n / denominador

H > 10

# com a precedência, podemos simplificar a expressão, incluindo a comparação
n / (1 / x1 + 1 / x2 + 1 / x3 + 1 / x4) > 10

# redefenindo o valor de H para facilitar os exemplos
H = int(input("Digite um valor: "))

# Estruturas de controle de fluco (ou condições/decisões)
if H > 10: # se a média harmônica for maior que 10
    print("Média harmôrnica maior que 10")
    # imprime 2 sempre
    # adicionado para exemplificar a execução de mais de uma instrução
    print (1 + 1)
# if H == 10:
elif H == 10:
    print("Média harmônica igual a 10")
elif H < 0:
    print ("Média harmônica negativa")
# if not (H > 10) or H!=10 or H>=0: # se a média harmôrnica for menor ou igual a 10    
else:
    print("Média harmônica menor ou igual a 10")

# sempre será impresso, mesmo que a condição seja falsa 
print("Fora do if/else")