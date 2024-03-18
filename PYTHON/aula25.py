# Introdução ao try/except

numero_str = input('Irei dobrar o numero que você digitar: ')


try:
    print(f'String: {numero_str}')
    numero = int(numero_str)
    print(f'Numero: {numero}')
    print(f'O dobro de {numero_str} é {numero * 2}')
except:
    print('Isso não é um número')