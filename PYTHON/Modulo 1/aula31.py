"""
Listas em Python
Tipo list - Mutável
Suporta vários valores de qualquer tipo
Conhecimentos reutilizáveis - índices e fatiamento
Métodos úteis:
    append, insert, pop, del, clear, extend, +
Create Read Update   Delete
Criar, ler, alterar, apagar = lista[i] (CRUD)
"""
#        0   1   2   3   4   5
lista = [10, 20, 30, 40]
# lista[2] = 300
# del lista[2]
# print(lista)
# print(lista[2])
lista.append(50) # adiciona valor ao final
lista.pop() # tira o valor do final
lista.append(60)
lista.append(70)
ultimo_valor = lista.pop(3) # o 'pop' retorna o valor.
#                   'pop(3)' pega o indice 3 e tira da lista
print(lista, 'Removido,', ultimo_valor)