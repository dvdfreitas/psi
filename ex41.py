def factorial(n):
    factorial = 1
    for i in range(1, n+1):
        factorial = factorial * i
    return factorial

def combinacao(n, r):
    return factorial(n) / (factorial(n-r) * factorial(r))

def b(r, n, p):
    combinacao(n, r) * (p ** r) * (1 - p) ** (n - r)

print(b(2, 10, 0.2))