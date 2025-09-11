def fatorial(n):
    if n == 0:
        return 1

    return n * fatorial(n-1)

def gerar_anagrama(p):
    n = len(p)
    if n == 1:
        return [p]
    resultado = []
    for i in range(n):
        ch = p[i]
        resto = p[:i] + p[i+1:]
        for perm in gerar_anagrama(resto):
            if ch+perm not in resultado:
                resultado.append(ch + perm)
    return resultado

result = gerar_anagrama('abc')

print(result)
print(len(result))
#  p     resto     return       resultado
# abc      bc                   [abc, acb, bac, bca, cab, cba]   (primeiro [char] mais o perm)
# abc tem 3 resultados possíveis de resto (obedecendo o while) que estão sendo ramificados em árvore
# bc       c      [bc, cb]       [bc, cb]              
# c                 [c]
# ac       c      [ac, ca]       [ac, ca]      
# c                 [c]
# ab       b                     [ab, ba]
# b                 [b]

#Cada uma das chamadas se ramifica em n partes, a depender do while que repete len(p) vezes.