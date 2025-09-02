n = int(input("Digite N para o total de números inteiros que vamos fazer a tabuada de 0 a 10: "))
i = 0
while i <= n:
    j = 0
    print(f'-------Tabuada do {i}-------\n')
    while j <= 10:
        prod = i * j
        print(f"{i} x {j} = {prod}")
        j += 1
    i += 1