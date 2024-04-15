''' == for loop nested ==

    Outer loop
        Inner loop                  '''

cores_time = ['Amarelo', 'Azul', 'Verde', 'Vermelho']

for partida in range(1, 11):
    print(f'Partida {partida} está começando e possui os times:')
    for cores in cores_time:
        print(cores)

# Neste exemplo usei um contexto onde temos um jogo iniciando várias partidas com cada partida
# contento seus times, tambem se aplicaria no contexto de: loja postando seus produtos e
# cada produto contendo suas características, comentários etc..
# py aula13.py