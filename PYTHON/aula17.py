
lines = int(input('Quantas linhas? '))
symbol = input('Qual simbolo? ')
print()
print(f'Gerando triângulo com {lines} linhas e feito com o caracter "{symbol[0]}"...')
print()

structure = 1

for line in range(lines):
    print((lines -1)*(' ') + (structure * f' {symbol[0]}'))
    lines -= 1
    structure += 1
print()

# Gerador de triangulos: escolha o numero de linhas e o simbolo que você desejar
# Obs: só ira aparecer o primeiro caracter que voce digitar
# py aula17.py