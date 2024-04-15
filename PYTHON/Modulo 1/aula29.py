#  Este é um código que faz algo semelhante ao da aula passada porém melhorado
# nesse exemplo, o código percorre toda a string e verifica a letra que mais se repete

frase = 'O Python é uma linguagem de programação ' \
    'multiparadigma. ' \
    'Python foi criado por Guido van Rossum'

i = 0
frequencia = 0
letramaisfrequente = ''
letra_atual = ''

while i < len(frase):
    letra_atual = frase[i]

    if letra_atual == ' ':
        i += 1
        continue

    if frequencia < frase.count(letra_atual):
        letramaisfrequente = letra_atual
        frequencia = frase.count(letra_atual)

    i += 1

print(f'A letra que mais repete é "{letramaisfrequente}" aparecendo {frequencia}x')
print()