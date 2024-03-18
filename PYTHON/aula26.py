"""
CONSTANTE = "Variáveis" que não vão mudar
Muitas condições no mesmo if (ruim)
    <- Contagem de complexidade (ruim)
"""
velocidade = 60  # velocidade atual do carro
local_carro = 100  # local em que o carro está na estrada

RADAR_1 = 60  # velocidade máxima do radar 1
LOCAL_1 = 100  # local onde o radar 1 está
RADAR_RANGE = 1  # A distância onde o radar pega

if 98 < local_carro < 102:
    if velocidade > (RADAR_1):
        print('Acima da velocidade permitida')
    else:
        print('Velocidade ok')
else:
    print('O carro não passou pelo radar 1')