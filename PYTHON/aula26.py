"""
Faça um programa que peça ao usuário para digitar um número inteiro,
informe se este número é par ou ímpar. Caso o usuário não digite um número
inteiro, informe que não é um número inteiro.
"""

numero_str = input('Digite um numero inteiro: ')
verifica_se_o_numero_é_int = type(numero_str)
numero_int = int(numero_str)

if numero_int:
    if int(numero_str) % 2 == 0:
        print(f'O número {numero_str} é par')
    else:
        print(f'O número {numero_str} não é par')
else:
    print('O numero não é um inteiro') 

"""
Faça um programa que pergunte a hora ao usuário e, baseando-se no horário 
descrito, exiba a saudação apropriada. Ex. 
Bom dia 0-11, Boa tarde 12-17 e Boa noite 18-23.
"""

"""
Faça um programa que peça o primeiro nome do usuário. Se o nome tiver 4 letras ou 
menos escreva "Seu nome é curto"; se tiver entre 5 e 6 letras, escreva 
"Seu nome é normal"; maior que 6 escreva "Seu nome é muito grande". 
"""