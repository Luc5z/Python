# listas enumeradas

lista = ['Maria', 'Helena', 'Luiz']
lista.append('Lucas')

lista_enumerada = enumerate(lista)
# recebe a lista e enumera cada item dela

lista_enumerada = list(lista_enumerada)

print('Agora isso é uma lista: ')
print(lista_enumerada)
print()

# truque:

for indice, nome in enumerate(lista):
    print(indice, nome)
print()