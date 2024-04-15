"""
Operação ternária (condicional de uma linha)
<valor> if <condicao> else <outro valor>
"""

condicao = 10 == 10
variavel = 'Valor' if condicao else 'Outro valor'
print(variavel)


print('Valor' if False else 'Outro valor' if False else 'Fim')