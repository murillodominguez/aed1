from math import sqrt

n = int(input("Informe o limite para checar quantos números primos existem: "))
i = 2
cont = 0
while i <= n:
    j = int(sqrt(i))
    primo = True 
    while j > 1:  
        if i % j == 0:
            primo = False
        j -= 1
    if primo:
        cont += 1
        print(i)
    i += 1
if cont == 0:
    print("Não há primos no intervalo.")