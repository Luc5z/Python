"""
Faça uma lista de compras com listas
O usuário deve ter a possibilidade de
inserir, apagar e listar valores da sua lista
Não permita que o programa quebre com 
erros de índices inexistentes na lista.
"""

import os

actions = 'ials'
toBuyList = []

while True:
    action = input('Selecione uma opção: \n[i]nserir [a]pagar [l]istar [s]air \n')

    if len(action) > 1 or action not in actions:
        print('Por favor digite uma opção válida.')
        print()
        continue
    
    if action == 'i':
        os.system('cls')
        valor = input('Valor: ')
        toBuyList.append(valor)
        print()

    elif action == 'a':
        os.system('cls')
        for index, item in enumerate(toBuyList):
            print(index, item)
        print()

        valor = input('O que você deseja apagar? ')
        try:
            toBuyList.pop(int(valor))
        except ValueError:
            print('Por favot digite um número Int.')
            print()
            continue
        except IndexError:
            print('Índice não existe na lista.')
            print()
            continue
        except Exception:
            print('Erro desconhecido.')
            print()
            continue

    elif action == 'l':
        os.system('cls')
        if toBuyList:
            for index, item in enumerate(toBuyList):
                print(index, item)
            print()
        else:
            print('Lista vazia.')
            print()
            continue

    elif action == 's':
        os.system('cls')
        print('Saindo...')
        print()
        break
