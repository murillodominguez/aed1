def is_balanceada(matriz):
    if len(matriz) != len(matriz[0]) or len(matriz) % 2 != 0:
        return 'ERRO: Não é uma matriz quadrada!'
    
    soma_quadrante_ant = 0
    soma_quadrante = 0
    quadrantes = 0

    i = 0
    j = 0


    while quadrantes < 4:
        if j == len(matriz)/2 or j == len(matriz):
            i += 1
            if j == len(matriz)/2:
                j = 0
            else:
                j = len(matriz)//2
            if i == len(matriz)/2 or i == len(matriz):
                if i == len(matriz):
                    i = 0
                    j = len(matriz)//2
                if soma_quadrante != soma_quadrante_ant and quadrantes > 0:
                    return False
                soma_quadrante_ant = soma_quadrante
                soma_quadrante = 0
                quadrantes += 1

        soma_quadrante += matriz[i][j]
        j += 1
    return True

    
matriz = [[1,3,5,6],[7,4,0,4],[3,3,6,7],[5,4,1,1]]

result = is_balanceada(matriz)

print(result)