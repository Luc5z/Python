# gerador de cpf

import random

cpf = ''

for i in range(9):
    cpf += str(random.randint(0, 9))

multiplicador = 10
soma_total = 0

for numero in cpf:
    soma_total += int(numero) * multiplicador

    multiplicador -= 1


primeiro_numero = (soma_total * 10) % 11

primeiro_numero = primeiro_numero if primeiro_numero <= 9 else 0

cpf = cpf + str(primeiro_numero)
# verificar o segundo digito do cpf

multiplicador = 11
soma_total = 0

for numero in cpf:
    soma_total += int(numero) * multiplicador

    multiplicador -= 1


segundo_numero = (soma_total * 10) % 11

segundo_numero = segundo_numero if segundo_numero <= 9 else 0


cpf = cpf + str(segundo_numero)

print(cpf)


