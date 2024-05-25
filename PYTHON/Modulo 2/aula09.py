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

numero = 1

print(f'Pergunta: {asks[1]["ask"]}')
print(f'Opções:')
for option in asks[1]['options']:
    print(f'{numero}) {option}')
    numero += 1




# reposta = input(f"{asks[1]['options']} ")

# if reposta == asks[1]['response']:
#     print('acertou')

