""" 
Resumo do que tem que ser feito:

Faça um jogo para o usuário adivinhar qual
a palavra secreta.
- Você vai propor uma palavra secreta
qualquer e vai dar a possibilidade para
o usuário digitar apenas uma letra.
- Quando o usuário digitar uma letra, você 
vai conferir se a letra digitada está
na palavra secreta.
    - Se a letra digitada estiver na
    palavra secreta; exiba a letra;
    - Se a letra digitada não estiver
    na palavra secreta; exiba *.
Faça a contagem de tentativas do seu
usuário.
"""

import os # 'os' é operational system que ja vem no python

palavra_secreta = 'dinheiro'
letras_acertadas = ''
tentativas = 0




letras_tentadas = ''

while True:

    letra = input('Digite uma letra: ')

    if len(letra) == '':
        print('Vazio.')
        continue

    elif len(letra) > 1:
        print('Digite apenas uma letra.')
        continue

    if letra in letras_acertadas:
        print('Você ja tentou essa letra.')
        continue
    
    tentativas += 1

    if letra in palavra_secreta: # verifica se o usuário acertou
        letras_acertadas += letra # adiciona aos acertos

    palavra_chute = ''

    # loop para formar a pala
    for indice in palavra_secreta: # 'indice' nesse caso será cada letra da palavra secreta
        if indice in letras_acertadas: # se a letra 'x' da palavra 'xyz' foi acertada
            palavra_chute += indice # adicione ao que ja tem

        else: # se não
            palavra_chute += '*' # bote isso no lugar

    if palavra_chute == palavra_secreta:
        os.system('cls') # aqui está a utilidade do 'os'. '.system' executa comando no terminal, \
        # nesse caso, limpando com 'clear'
        print(f'Acertou! "{palavra_chute}" é a palavra secreta')
        print(f'Tentativas: {tentativas}')
        print()
        break

    print(palavra_chute)