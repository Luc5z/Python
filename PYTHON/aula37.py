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

# tratamento do CPF:
#      012 345 678 9
cpf = '957.667.620-70'

cpf = cpf.replace('.', '').replace('-', '')

# Algoritmo do cpf (1/2)
multiplicador = 10
numeros_multiplicados = []

for numero in cpf[:9]:
    # cpf: 95766762070
    numero = int(numero)
    numero_multiplicado = numero * multiplicador

    multiplicador -= 1

    numeros_multiplicados.append(numero_multiplicado)

soma_total = sum(numeros_multiplicados) * 10

resto_da_divisao_por_11 = soma_total % 11

primeiro_numero = resto_da_divisao_por_11 if resto_da_divisao_por_11 <= 9 else 0

# verificar se o primeiro numero do CPF passado está correto

if int(cpf[9]) == primeiro_numero:
    print(f'O primeiro numero está certo! {cpf[9]}')
else:
    print(f'O primeiro numero não está certo: {primeiro_numero} != {cpf[9]}')

print()
