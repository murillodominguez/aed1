# 19. Flatten de Lista Aninhada
# Escreva `flatten(lista)` que receba uma lista com sublistas aninhadas de profundidade
# arbitrária e retorne uma lista "achatada".
# Exemplo:
# Entrada: [1, [2, [3, 4]], 5]
# Saída: [1,2,3,4,5]

def flatten(lista):
    result = []
    for item in lista:
        if isinstance(item, list):
            result += flatten(item)
        else:
            result.append(item)
    print(result)
    return result

lista = [1, [2, [3, 4]], 5]
result = flatten(lista)

print(result)