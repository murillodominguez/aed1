#6 - Soma dos divisores de um número

n = int(input("Informe um número para somarmos seus divisores: "))

somadiv = 0
c = n//2
while c > 0:
    if n % c == 0:
        somadiv += c
    c -= 1

print(somadiv)