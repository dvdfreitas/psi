print("Insira o número:")
numero = int(input())

primo = True
n_dividir = range(2, numero)
for n in n_dividir:
    if numero % n == 0:
        primo = False
        break

if primo:
    print("É primo")
else:
    print("Não é primo")