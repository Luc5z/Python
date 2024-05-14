# Closure 

def criar_saudacao(saudacao, nome):
    def saudar():

        return f'{saudacao}, {nome}!'
    return saudar # retorna a função estruturada mas não executada

s1 = criar_saudacao('Bom dia', 'luiz') 
s2 = criar_saudacao('Bom dia', 'lucas') 

print(s1()) # executa a função
print(s2())