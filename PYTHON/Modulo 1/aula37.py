"""
Calculo do primeiro dígito do CPF
CPF: 746.824.890-70
Colete a soma dos 9 primeiros dígitos do CPF
multiplicando cada um dos valores por uma
contagem regressiva começando de 10

Ex.:  746.824.890-70 (746824890)
   10  9  8  7  6  5  4  3  2
*  7   4  6  8  2  4  8  9  0
   70  36 48 56 12 20 32 27 0

Somar todos os resultados: 
70+36+48+56+12+20+32+27+0 = 301
Multiplicar o resultado anterior por 10
301 * 10 = 3010
Obter o resto da divisão da conta anterior por 11
3010 % 11 = 7
Se o resultado anterior for maior que 9:
    resultado é 0
contrário disso:
    resultado é o valor da conta

O primeiro dígito do CPF é 7
""" 

import re # expressão regular
import sys 

# tratamento do CPF:
#      012 345 678 9
print('CPF Validator')
cpf = input('CPF: ')
print()

cpf = re.sub( r'[^0-9]','' , cpf) # isso filtra qualquer coisa que não seja um número

cpf_repetido = cpf == cpf[0] * len(cpf)

if cpf_repetido:
    print('Você enviou dados sequenciais')
    sys.exit()



# Algoritmo do cpf (1/2)
multiplicador = 10
soma_total = 0

for numero in cpf[:9]:
    # cpf: 95766762070
    soma_total += int(numero) * multiplicador

    multiplicador -= 1


primeiro_numero = (soma_total * 10) % 11

primeiro_numero = primeiro_numero if primeiro_numero <= 9 else 0

# verificar o segundo digito do cpf

multiplicador = 11
soma_total = 0

for numero in cpf[:10]:
    # cpf: 95766762070
    soma_total += int(numero) * multiplicador

    multiplicador -= 1


segundo_numero = (soma_total * 10) % 11

segundo_numero = segundo_numero if segundo_numero <= 9 else 0

cpf_temp = cpf[:9]
cpf_temp = cpf_temp + str(primeiro_numero) + str(segundo_numero)


if cpf == cpf_temp:
    print(f'O CPF {cpf} é válido')
else:
    print(f'O CPF não é válido')

print()
