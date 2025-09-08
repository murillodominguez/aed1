# 13. Multiplicação de Matrizes
# Escreva uma função `multiplicar_matrizes(A, B)` que multiplique duas matrizes (validando
# dimensões) e retorne o resultado.
# Exemplo:
# Entrada: A=[[1,2],[3,4]], B=[[2,0],[1,2]]
# Saída: [[4,4],[10,8]]

def multiplicar_matrizes(a,b):
    if len(a) == 0 or len(b) == 0:
        return "Matrizes vazias não podem ser multiplicadas"
    prev_len = len(a[0])
    for row in a:
        if len(row) != prev_len:
            return "Matrizes devem ter o mesmo número de colunas por linha"
        prev_len = len(row)
    prev_len = len(b[0])
    for row in b:
        if len(row) != prev_len:
            return "Matrizes devem ter o mesmo número de colunas por linha"
        prev_len = len(row)

    if len(a[0]) != len(b):
        return "Dimensões inválidas para multiplicação (A e B devem ter o mesmo número de colunas e linhas, respectivamente)"
    
    result = []
    
    i = 0
    while i < len(a):
        row = []
        j = 0
        while j < len(b):
            k = 0
            item = 0
            while k < len(a[0]):
                item += a[i][k] * b[k][j]
                k += 1
            row.append(item)
            print(item)
            j += 1
        result.append(row)
        i += 1
    
    return result

    
    
a = [[1,2,3], [3,4,5]]
b = [[2,0,3], [1,2,4], [1,1,5]]
result = multiplicar_matrizes(a,b)
print(result)