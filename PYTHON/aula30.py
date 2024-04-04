"""
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

import os

palavra_secreta = 'palavra'
letras_acertadas = ''
tentativas = 0


while True:

    letra = input('Digite uma letra: ')

    if len(letra) > 1:
        print('Digite apenas uma letra.')
        continue

    if letra in letras_acertadas:
        print('Você ja tentou essa letra.')
        continue
    
    tentativas += 1

    if letra in palavra_secreta:
        letras_acertadas += letra

    palavra_formada = ''

    for indice in palavra_secreta:
        if indice in letras_acertadas:
            palavra_formada += indice

        else:
            palavra_formada += '*'

    if palavra_formada == palavra_secreta:
        os.system('clear')
        print(f'Acertou! "{palavra_formada}" é a palavra secreta')
        print(f'Tentativas: {tentativas}')
        print()
        break

    print(palavra_formada)