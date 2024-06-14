def executa(funcao, *args):
    return funcao(*args)

print(executa(lambda x, y: x + y, 2, 3)) # Embaixo veja isso em uma versão mais explicada

print(
    executa(
      # nome parametro corpo 
        lambda x, y: x + y,     # Função
        2, 3                    # Argumentos
    )
)

print(
    executa(
        lambda *args: sum(args),
        1, 2, 3, 4, 5, 6, 7
    )
)