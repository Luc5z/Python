# Exercício - sistema de perguntas e respostas


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

for pergunta in asks:
    print('Pergunta:', pergunta['ask'])
    print()

    opcoes = pergunta['options']
    for i, opcao in enumerate(pergunta['options']):
        print(f'{i})', opcao)
    print()

    escolha = input('Escolha uma opção: ')

    acertou = False
    escolha_int = None
    qtd_opcoes = len(opcoes)

    if escolha.isdigit():
        escolha_int = int(escolha)

    if escolha_int != None:



# reposta = input(f"{asks[1]['options']} ")

# if reposta == asks[1]['response']:
#     print('acertou')

