from math import sqrt

def is_primo(n):
    if n <= 1:
        return False
    i = int(sqrt(n))
    while i > 1:
        if n % i == 0:
            return False
        i -= 1
    return True

n = int(input("Digite um número: "))

if is_primo(n):
    print(f'{n} é primo.')
else:
    print(f'{n} não é primo.')