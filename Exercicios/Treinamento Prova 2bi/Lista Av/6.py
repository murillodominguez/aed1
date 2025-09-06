def fatorial(n):
    if n == 0:
        return 1

    return n * fatorial(n-1)

def gerar_anagrama(p):
    n = len(p)
    if n <= 1:
        return [p]
    resultado = []
    for i in range(n):
        ch = p[i]
        resto = p[:i] + p[i+1:]
        print(gerar_anagrama(resto))
        for perm in gerar_anagrama(resto):
            resultado.append(ch + perm)
    return resultado

result = gerar_anagrama('ab')

print(result)
        