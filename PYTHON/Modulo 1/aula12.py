# Enviar um email com os detalhes da compra online (Maximo 3 tentativas)

compra_confirmada = False
dados_compra = 'Compra no valor de R$12.50 e entrega confirmada'

for enviar in range(3): # for loop + if/else juntos para tentar 3 vezes SE a compra_confirmada for "False"
    if compra_confirmada:
        print(dados_compra)
        print('Detalhes enviado para o seu email')
        break # Break interrompe o loop se a compra_confirmada for "True" impedindo de se repetir a mensagem
else:
    print('Falha na compra')
    
# py aula12.py