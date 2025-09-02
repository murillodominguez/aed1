from math import sqrt

def find_primos(n, i = 2, primos = []):
    if n <= 1:
        return primos
    for x in primos:
        if i % x == 0:
            return find_primos(n-1, i+1, primos)
    primos.append(i)
    return find_primos(n-1, i+1, primos)
    
print(find_primos(80))