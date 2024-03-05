# Functions
# DRY - Don't repeat yourself.

# parametro -> argumento

def boas_vindas():
    print('Olá Lucas!')
    print('Temos 5 laptops em estoque')

boas_vindas() # para chamar uma função


def boas_vindas_v2(nome, quantidade): # argumentos para funçao funcionar
    print(f'Olá {nome}!')
    print(f'Temos {quantidade} laptops em estoque')

boas_vindas_v2('Lucas', 5) # chamando a funcao com os argumentos que eu quero utilizar

# py aula18.py