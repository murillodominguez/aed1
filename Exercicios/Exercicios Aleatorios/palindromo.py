#2 - Palindromos 1 a 1000

#Função que retornaria o inverso
# def monta_inv(n):
#     if n/10 < 1:
#         return n
    
#     inv = 0
#     while n > 0:
#         inv = inv*10 + n%10
#         n = n//10
#     return inv

#Código que importa

c = 1

while c <= 1000:
    n = c
    if c/10 < 1:
        inverso = n
    else:
        inverso = 0
        while n > 0:
            inverso = inverso*10 + n%10
            n = n//10
    if inverso == c:
        print(c)
    c += 1