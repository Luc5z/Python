# fatiamento de strings
#  012345678 --> indice
#  Olá mundo
# -987654321
# Fatiamento [i:f:p] [::]
# Obs.: a função len retorna a qtd
# de caracteres da str

variavel = 'Olá mundo'
print(variavel[-8:-2])
print(variavel[4:])
print(variavel[:-6])
print(variavel[::-1]) # aqui irá ir do inicio ao fim porem contando de tras pra frente
print(len(variavel))