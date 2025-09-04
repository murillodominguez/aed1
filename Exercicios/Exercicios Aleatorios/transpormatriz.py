# Implemente `transpor(matriz)` que receba uma matriz (lista de listas) e retorne sua
# transposta.​
# ​
# Exemplo:​
# Entrada: [[1,2,3],[4,5,6]]​
# Saída: [[1,4],[2,5],[3,6]]

def transpor(matriz):
    tamanho = len(matriz[0])
    matriz_transposta = []
    i = 0
    while i < tamanho:
        item = []
        j = 0
        while j < len(matriz):
            item.append(matriz[j][i])
            if len(matriz[j]) != tamanho:
                return 'As linhas da matriz não podem ser de tamanhos diferentes!'
            j += 1
        matriz_transposta.append(item)
        i += 1
    return matriz_transposta

matriz = [[1,2,3], [4, 5, 6], [7, 8, 9]]

print(transpor(matriz))