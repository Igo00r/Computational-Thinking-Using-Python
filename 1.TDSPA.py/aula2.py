x= input()

X = x.upper()  # tudo maiúsculo

print("entrada: ", x)
print("entrada em maiúsculo: ", X)


texto = "Igoorr" # string
inteiro = 10
real = 3.14 # float
booleano_verdadeiro = True # bool
booelano_falso = False # bool

type(texto)

# string -> str
# inteiro -> int
# real -> float
# booleano -> bool

# casting 
# str -> float
float ("3.14")
#str -> int
int ("10")

#float -> int
int(3.14)
# int -> float
float(10) # 10.0

# int -> str 
str(10)   # "10"
# floatr -> str
str(3.14) # "3.14"

# str -> bool
bool("True") # True
bool("False") # True
bool("") # False

# int -> bool
bool(0) # False
bool(1) # True
bool(-1) # True

# float -> bool
bool(0.0) # False
bool(0.1) # True
bool(-0.1) # True

#Operações aritméticas

# soma
10 + 5 # 15
# subtração
10 - 5 # 5
# multiplicação
10 * 5  # 50
# divisão 
10 / 5 # 2.0
# divisão inteira
10 // 5 # 2 -> motivo: 10 = 5*2 + 0
11 // 5 # 2 -> motivo 11 = 5*2 = 1
# resto da divisão ou módulo
10 % 5 # 0 -> motivo: 10 = 5*2 + 0
11 % 5 # 1 -> motivo: 11 = 5*2 + 0 
# avaliando se é par ou ímpar
10 % 2 # 0 -> par
11 % 2 # 1 -> ímpar

# potência
10**2 # 100 -> mesmo que 10*10 ou 10^2 ou 10 elevado a 2 
10**5 # 100000 -> mesmo que 10*10*10*10*10 ou 10^5 ou 10 elevado a 5

# raiz quadrada
100**0.5 # 10.0
# motivo: todo número elevado a 0.5 é a raiz quadrada, ou seja, 100^(1/2) = 10

# OPERADORES LÓGICOS
# sempre retornam True ou False

# Operações de comparação

#NUMÉRICOS
# igualdade:
#   - sempre utilizar == e não =, pois = é utilizado para atibuição
#   - atribuição é quando você quer atribuir ("guardar") um valor numa variável
10 == 5 # False
10 == 10 # True

# diferença; é o inverso da igualdade
10 != 5 # True
10 != 10 # False

# maior
10 > 5 # True
10 > 10 # False
10 > 11 # False
# menor
10 < 5 # False
10 < 10 # False
10 < 11 # True
# maior ou igual
10 <= 5 # False
10 <= 10 # True
10 < 11 # True

# menor ou igual
10 <= 5 # False
10 <= 10 # True
10 <= 11 # True

# LÓGICOS
# and: retorna True se as duas condições forem verdadeiras 
# or: retorna True se pelo menos uma das condições for verdadeira
# not: inverte o valor da condição

# Operator "and"
True and True # True
True and False # False
False and True # False
False and False # False
# É  similar a multiplicação, pois se um dos elemoentos for zero, o resultado é zero
# 1 * 1 -> 1 
# 1 * 0 -> 0
# 0 * 1 -> 0
# 0 * 0 -> 0

# Operador "or"
True and True # True
True and False # True
False and True # True
False and False # False
# É similar a soma, pois se um dos elementos for um, o resultador é um
# 1 + 1 -> 1
# 1 + 0 -> 1 
# 0 + 1 -> 0
# 0 + 0 -> 0

# Operador "not"
not True # False
not False # True
# É similar a multiplicação por -1
# -1 * 1 -> -1
# -1 * 1 -> 1

# Exemplo
not (10 == 5) # not False -> True, efeito prático: mesmo que 10 != 5
not (10 == 10) # not True -> False, efeito prático: mesmo que 10 != 10

# Retomando o exemplo do IMC:
peso = 90 # kg
altura = 1.75 # m
imc = peso / (altura**2) # 26.122448979591837
round (imc, 2) #26.12   # arredondando para duas casas decimais
print (F"IMC: {imc: .2f}")
imc < 18.5 # False
imc <= 18.5 and imc < 25 # False
imc >= 25 and imc < 30 # True
imc >= 30 # False

# Operações 