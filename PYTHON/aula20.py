# Calcula e retorna um valor (Armazenar)

def cliente1(nome):
    print(f'Ola {nome}') # <-- Executa e descarta o valor

def cliente2(nome):
    return f'Ola {nome}' # <--  Apenas armazena o valor

x = cliente1('Luisa') # isso ira executar a funcao sem guardar nenhum valor
y = cliente2('Lucas')

cliente1('Luisa') # ira imprimir "Ola luisa" e nao guardar nenhum valor
cliente2('Lucas') # isso não ira imprimir nada, porem ira guardar o valor
print(x) # isso imprime "none" pois nao tem como guardar o valor
print(y) # isso ira imprimir o resultado de 'cliente2('Lucas')' guardado na variavel y

# * Importante: saber usar o print() e o return nas horas certas
# py aula20.py