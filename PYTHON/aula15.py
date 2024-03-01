linhas = input('Quantas linhas? ')
colunas = input('Quantas colunas? ')
simbolo =  input('Qual o simbolo?(Sera considerado o primeiro simbolo que digitar) ')

for l in range(int(linhas)):
    for c in range(int(colunas)):
        print(f' {simbolo[0]}', end='') # --> f'' para ter um espaço entre os simbolos
    print() # imprime um Enter <--        --> [0] para pegar apenas o 1° caracter que for digitado

# py aula15.py