# 11. Matriz Identidade
# Crie uma função `matriz_identidade(n)` que receba um número inteiro `n` e retorne uma
# lista de listas representando uma matriz identidade de tamanho `n`.
# Exemplo:
# Entrada: 3
# Saída: [[1,0,0],[0,1,0],[0,0,1]]

def matriz_identidade(n):
    matriz = []
    i = 0
    while i < n:
        row = []
        j = 0
        while j < n:
            if j == i:
                row += [1]
            else:
                row += [0]
            j += 1
        matriz += [row]
        i += 1
    return matriz

print(matriz_identidade(3))  # Saída: [[1,0,0],[0,1,0],[0,0,1]]

print(matriz_identidade(5))