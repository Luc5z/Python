# xargs: botar uma quantidade x de parametros no argumento da funcao

def soma_de_numeros(*numeros): # O " * " faz a variavel numeros receber qualquer quantidade de variavel
    resultado = 0 # inicializando a variavel
    for numero in numeros:
        resultado += numero
    return resultado # Uso do return para armazenar o resultado <-

soma = soma_de_numeros(10, 20, 30, 40, 50) # = 150

print(soma) # vai imprimir o valor guardado na variavel soma  (150)

# py aula21.py