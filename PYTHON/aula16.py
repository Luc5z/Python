# Contexto: uma loja quer fazer uma promoção onde venda
#  um produto 5 reais mais barato a cada dia (até 25 reais para nao sair no prejuízo)

valor = 100
dia = 1

while valor > 20: # enquanto a condição for verdadeira ele irá executar
    print(f'No dia {dia} o produto será vendido por R${valor}')
    dia += 1    # forma mais limpa de dizer "dia = dia + 1" 
    if valor - 5 > 20:
        valor -= 5  # forma mais limpa de dizer "valor = valor - 5"
    else:
        break 

# py aula16.py 