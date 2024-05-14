# crie funções que duplicam, triplicam e quadriplicam
# exercicio feito compactado usando closure

def operations(operation):
    def operate(number):
        return f'{int(operation) * int(number)}'
    return operate

duplicar = operations(2)
triplicar = operations(3)
quadruplicar = operations(4)

print(duplicar(3))
print(triplicar(3))
print(quadruplicar(3))