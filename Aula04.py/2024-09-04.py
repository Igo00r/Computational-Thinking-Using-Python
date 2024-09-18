# OPERADORES LÓGICOS
# sempre retornam True ou False

# Operações de comparação

# NUMÉRICOS
# igualdade:
#   - sempre utilizar == e não =, pois = é utilizado para atribuição
#   - atribuição é quando você quer atribuir ("guardar") um valor numa variável
10 == 5  # False
10 == 10  # True

# diferença: é o inverso da igualdade
10 != 5  # True
10 != 10  # False

# maior
10 > 5  # True
10 > 10  # False
10 > 11  # False
# menor
10 < 5  # False
10 < 10  # False
10 < 11  # True

# maior ou igual
10 >= 5  # True
10 >= 10  # True
10 >= 11  # False

# menor ou igual
10 <= 5  # False
10 <= 10  # True
10 <= 11  # True

# LÓGICOS
# and: retorna True se as duas condições forem verdadeiras
# or: retorna True se pelo menos uma das condições for verdadeira
# not: inverte o valor da condição

# Operador "and"
True and True  # True
True and False  # False
False and True  # False
False and False  # False
# É similar a multiplicação, pois se um dos elementos for zero, o resultado é zero
# 1 * 1 -> 1
# 1 * 0 -> 0
# 0 * 1 -> 0
# 0 * 0 -> 0

# Operador "or"
True or True  # True
True or False  # True
False or True  # True
False or False  # False
# É similar a soma, pois se um dos elementos for um, o resultado é um
# 1 + 1 -> 1
# 1 + 0 -> 1
# 0 + 1 -> 1
# 0 + 0 -> 0

# Operador "not"
not True  # False
not False  # True
# É similar a multiplicação por -1
# -1 * 1 -> -1
# -1 * -1 -> 1

# Exemplo
not (10 == 5)  # not False -> True, efeito prático: mesmo que 10 != 5
not (10 == 10)  # not True -> False, efeito prático: mesmo que 10 != 10

# Retomando o exemplo do IMC:
peso = 80  # kg
altura = 1.75  # m
imc = peso / (altura**2)  # 26.122448979591837
round(imc, 2)  # 26.12  # arredondando para duas casas decimais
print(f"IMC: {imc:.2f}")
imc < 18.5  # False
imc >= 18.5 and imc < 25  # False
imc >= 25 and imc < 30  # True
imc >= 30  # False


# Operações com strings
# igualdade
"python" == "python"  # True
"python" == "Python"  # False

# diferença
"python" != "python"  # False
"python" != "Python"  # True

# maior
"python" > "python"  # False
"python" > "Python"  # True

# menor
"python" < "python"  # False
"python" < "Python"  # False

# maior ou igual
"python" >= "python"  # True
"python" >= "Python"  # True

# menor ou igual
"python" <= "python"  # True
"python" <= "Python"  # False

# Operadores lógicos
# and
"python" == "python" and "Python" == "Python"  # True
"python" == "python" and "Python" == "python"  # False
# or
"python" == "python" or "Python" == "Python"  # True
"python" == "python" or "Python" == "python"  # True
"python" == "Python" or "Python" == "python"  # False

# not
not "python" == "python"  # False
not "python" == "Python"  # True

# Operações "aritméticas" com strings
# adição -> concatenação (nome mais correto tecnicamente)
"python" + " é legal"  # "python é legal"  # tinha um espaço no início de ' é legal'
"python" + "é " + "legal"  # "pythoné legal" # não tem espaço entre 'python' e 'é'

# subtração e divisão não fazem sentido para strings
# multiplicação
"python" * 3  # "pythonpythonpython", ou seja, repete a string 3 vezes,
# similar a "python" + "python" + "python"
"python " * 3  # "python python python ", ou seja, repete a string 3 vezes,
# similar a "python " + "python " + "python "
