l1 = [1, 2, 3, 4]
l2 = [1, 2, 3, 4]

def zipper(lista1, lista2):
    intervalo_maximo = min(len(lista1), len(lista2))
    return[
        (lista1[i] + lista2[i]) for i in range(intervalo_maximo)
    ]

print(zipper(l1, l2))