frase = 'O Python é uma linguagem de programação ' \
    'multiparadigma. ' \
    'Python foi criado por Guido van Rossum'

i = 0
while i < len(frase):
    letra_atual = frase[i]

    print(letra_atual, frase.count(letra_atual))

    i += 1