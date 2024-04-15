"""
Faça um programa que peça ao usuário para digitar um número inteiro,
informe se este número é par ou ímpar. Caso o usuário não digite um número
inteiro, informe que não é um número inteiro.
"""

numero_str = input('Digite um numero inteiro: ')
verifica_numero = numero_str.isdigit()

if verifica_numero:
    if int(numero_str) % 2 == 0:
        print(f'O número {numero_str} é par')
    else:
        print(f'O número {numero_str} é ímpar')
else:
    print(f'{numero_str} não é um inteiro') 

"""
Faça um programa que pergunte a hora ao usuário e, baseando-se no horário 
descrito, exiba a saudação apropriada. Ex. 
Bom dia 0-11, Boa tarde 12-17 e Boa noite 18-23.
"""

horaUsuario = int(input('Que horas são? '))

if 0 <= horaUsuario <= 11:
    print('Bom dia!')
elif 12 <= horaUsuario <= 17:
    print('Boa tarde!')
elif 18 <= horaUsuario <= 23:
    print('Boa noite!')
else:
    print('Erro')

"""
Faça um programa que peça o primeiro nome do usuário. Se o nome tiver 4 letras ou 
menos escreva "Seu nome é curto"; se tiver entre 5 e 6 letras, escreva 
"Seu nome é normal"; maior que 6 escreva "Seu nome é muito grande". 
"""

nome = input('Qual seu primeiro nome? ')

if len(nome) <= 4:
    print('Seu nome é muito curto')
elif 5 <= len(nome) <= 6:
    print('Seu nome é normal')
else:
    print('Seu nome é muito grande')