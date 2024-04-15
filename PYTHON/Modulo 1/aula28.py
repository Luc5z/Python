# Este código verifica a quantidade de vezes em que uma letra se repete na "frase"

frase = 'O Python é uma linguagem de programação ' \
    'multiparadigma. ' \
    'Python foi criado por Guido van Rossum'

frasemanipulada = frase.lower()

letra = 'o'
numeroletras = frasemanipulada.count(letra)
print(f'a frase tem {numeroletras} letras {letra}')