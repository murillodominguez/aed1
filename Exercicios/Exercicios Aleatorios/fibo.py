#3 - Fibonacci sem recursividade nem função = sofrimento

n = int(input("Informe até onde vamos com essa Fibonacci: "))
c = 0
num = 0
aux1 = 0
aux2 = 1
while c < n:
    if c == 0:
        num = c
    else:
        if c%2 == 0:
            aux1 = num
        else:
            aux2 = num
        if c < 3:
            num = 1
        else:
            num = aux1 + aux2
    print(num)
    c += 1