print("Introduza a string", end=' ')
string = input()

contar_a = 0
for letra in string:
    if letra == "a":
        contar_a = contar_a + 1

print("O número de letras a é", contar_a)