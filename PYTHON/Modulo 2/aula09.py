# Exercício - sistema de perguntas e respostas
import os

asks = [
    {
        'ask': 'Quanto é 2+2?',
        'options': ['1', '3', '4', '5'],
        'response': '4',
    },
    {
        'ask': 'Quanto é 5*5?',
        'options': ['25', '55', '10', '51'],
        'response': '25',
    },
    {
        'ask': 'Quanto é 10/2?',
        'options': ['4', '5', '2', '1'],
        'response': '5',
    },
]

resultado = 0

for pergunta in asks:
    print('Pergunta:', pergunta['ask'])
    print()

    opcoes = pergunta['options']
    for i, opcao in enumerate(pergunta['options']):
        print(f'{i})', opcao)
        resposta = pergunta['response']
    print()

    escolha = input('Escolha uma opção: ')

    escolha_int = None
    qtd_opcoes = len(opcoes)

    if escolha.isdigit():
        escolha_int = int(escolha)

    if escolha_int != None:
        if 0 <= escolha_int < qtd_opcoes:
            escolha_int = pergunta['options'][escolha_int]

            os.system('cls')

            if escolha_int == resposta:
                resultado += 1

                print()
                print('Acertou!')
                print()

            else: 

                print()
                print('Errou..')
                print()
        else:
            os.system('cls')
            print()
            print('escolha inválida')
            print()
            break

print(f'Resultado: {resultado}')
print()
