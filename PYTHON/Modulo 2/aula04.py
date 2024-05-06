# Exercícios com funções

# Crie uma função que multiplica todos os argumentos
# não nomeados recebidos
# Retorne o total para uma variável e mostre o valor
# da variável.

def soma(*args):
    total = 1
    for numero in args:
        total *= numero
    print(total)

# Crie uma função fala se um número é par ou ímpar.
# Retorne se o número é par ou ímpar.

def is_even(number):
    if number % 2 == 0:
        return f'O número {number} é par'

    return f'O número {number} é impar'

soma(1, 2, 3, 4, 5)
print(is_even(1))