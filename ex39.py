print("Introduza o número:")
numero = int(input())

mult = 1
for n in range(1, numero+1):
    mult = mult * n

print("O factor é: " + str(mult))