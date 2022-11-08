dias = [
    'segunda-feira', 
    'terça-feira', 
    'quarta-feira', 
    'quinta-feira',
    'sexta-feira',
    'sábado',
    'domingo'
]

n_clientes = [
    105,
    101,
    102,
    103,
    104,
    105,
    107
]

print(dias[0])
print(dias[2])
# print(dias[4]) # Esta posição não existe (ultrapassou - vai dar erro)

for i in range(0, len(dias)):
    print(dias[i])

soma = 0
for i in range(0, len(dias)):
    soma = soma + n_clientes[i]
    print(dias[i] + ": " + str(n_clientes[i]))
print("------------")
print("Soma: " + str(soma))
