# 16. Espiral de Números
# Escreva uma função `matriz_espiral(n)` que construa uma matriz `n x n` preenchida com
# números de 1 a `n²`, em ordem espiral.
# Exemplo:
# Entrada: 3
# Saída:
# [[1,2,3],[8,9,4],[7,6,5]]

#1 2 3    1 2 3
#8 9 4    4 5 6
#7 6 5    7 8 9

# Versão IMBECIL (resolve outro problema)
def matriz_espiral_diferente(n):
    matriz = []
    i = 0
    k = 1
    while i < n:
        row = []
        j = 0
        while j < n:
            row += [k]
            k += 1
            j += 1
        i += 1
        matriz.append(row)

    espiral = []
    right_wall = len(matriz[0]) - 1
    bottom_wall = len(matriz) - 1
    left_wall = 0
    upper_wall = 1
    direction = "RIGHT"


    i = 0
    j = 0
    k = 0
    while k < len(matriz):
        row = []
        while len(row) < len(matriz[0]):
            row += [matriz[i][j]]
            if direction == "RIGHT":
                if j == right_wall:
                    right_wall -= 1
                    direction = "DOWN"
                else:
                    j += 1
            if direction == "DOWN":
                if i == bottom_wall:
                    bottom_wall -= 1
                    direction = "LEFT"
                else:
                    i += 1
            if direction == "LEFT":
                if j == left_wall:
                    left_wall += 1
                    direction = "UP"
                else:
                    j -= 1
            if direction == "UP":
                if i == upper_wall:
                    upper_wall += 1
                    j += 1
                    direction = "RIGHT"
                else:
                    i -= 1
        espiral += [row]
        k += 1

    return espiral

espiral = matriz_espiral_diferente(6)
print(f'Espiral Diferente: {espiral}\n')

#01 02 03 04 05 06
#07 08 09 10 11 12
#13 14 15 16 17 18
#19 20 21 22 23 24
#25 26 27 28 29 30
#31 32 33 34 35 36

def matriz_espiral(n):
    matriz_base = []
    i = 0
    while i < n:
        row = []
        j = 0
        while j < n:
            row += [0]
            j += 1
        matriz_base += [row]
        i += 1
    
    k = 1
    i = 0
    j = 0
    right_wall = len(matriz_base[0]) - 1
    bottom_wall = len(matriz_base) - 1
    left_wall = 0
    upper_wall = 1

    direction = "RIGHT"
    while k <= n*n:
        matriz_base[i][j] = k
        if direction == "RIGHT":
            if j == right_wall:
                right_wall -= 1
                direction = "DOWN"
            else:
                j += 1
        if direction == "DOWN":
            if i == bottom_wall:
                bottom_wall -= 1
                direction = "LEFT"
            else:
                i += 1
        if direction == "LEFT":
            if j == left_wall:
                left_wall += 1
                direction = "UP"
            else:
                j -= 1
        if direction == "UP":
            if i == upper_wall:
                upper_wall += 1
                j += 1
                direction = "RIGHT"
            else:
                i -= 1
        k += 1
    return matriz_base

espiral = matriz_espiral(6)
print(f'Espiral como o exercício pede: {espiral}')

# 01 02 03 04 05 06
# 20 21 22 23 24 07
# 19 32 33 34 25 08
# 18 31 36 35 26 09
# 17 30 29 28 27 10
# 16 15 14 13 12 11