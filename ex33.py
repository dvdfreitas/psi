################
# Exercício 33 #
################
# Sabendo que:
# 1 polegada (in) = 2,54 cm
# 1 pé (ft) = 30,48 cm
# Elabore um programa que permita ao utilizador converter polegadas e pés para centímetros. 

print("Introduza um número:")
numero = int(input())

print("1 - Converter de polegadas para cms")
print("2 - Converter de pés para cms")
print("Opção: ")
opcao = int(input())

if opcao == 1:
    resultado = numero * 2.54
elif opcao == 2:
    resultado = numero * 30.48

print("Resultado: " + str(resultado))
