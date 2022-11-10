# Esta função calcula se um número é primo
# e retorna um valor True ou False
def verifica_se_primo(n):
    primo = True
    for i in range(2, n):
        if n % i == 0:
            primo = False
    return primo

print("Até que número quer calcular os primos")
n = int(input())
total_primos = 0
for i in range(1, n+1):
    if verifica_se_primo(i):
        #print(i)
        total_primos = total_primos + 1

print("Total de primos: " + str(total_primos))
percentagem = (total_primos / n) * 100
print("Percentagem " + str(percentagem))