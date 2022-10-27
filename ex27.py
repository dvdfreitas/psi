print("Introduza o primeiro número")
n1 = int(input())
print("Introduza o segundo número")
n2 = int(input())
print("Introduza o terceiro número")
n3 = int(input())

if n1 >= n2 and n1 >= n3:
    maior = n1
elif n2 >= n1 and n2 >= n3:
    maior = n2
else:
    maior = n3

print(maior)