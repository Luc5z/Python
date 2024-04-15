# Non-Default: Aquele que voce nao define o valor no parametro
# Regra: non-default vem primeiro do que os default sempre


def boas_vindas(nome, quantidade=6): # quando voce define um argumento aqui nao precisa preenche-lo ao chamar a funcao
    print(f'Olá {nome}!')
    print(f'Temos {quantidade} laptops em estoques')

boas_vindas('Lucas') # funcao + parametro


# argumento recebe parametro
# py aula19.py