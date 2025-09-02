n = float(input("Digite um número para retornar sua tabuada de 0 a 100: "))
m = 0
while m <= 100:
    result = n * m
    print(f"{n} x {m} = {result}")
    m += 1