velocidade_pista = 100
velocidade = int(input('Qual a sua velocidade? '))

if velocidade > velocidade_pista:
    print('Acima da velocidade permitida')
    print('Favor reduzir sua velocidade')
elif velocidade <= 60:
    print('Velocidade abaixo da média')
    print('Favor dirigir acima de 80Km/h')
else:
    print('Velocidade OK')


# Introdução a condicionais e identação
# py aula9.py

