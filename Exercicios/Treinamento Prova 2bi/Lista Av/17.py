# 17. Rotação de Lista
# Implemente `rotacionar(lista, k)` que rotacione os elementos de uma lista `k` posições à
# direita usando apenas laços.
# Exemplo:
# Entrada: ([1,2,3,4,5], 2)
# Saída: [4,5,1,2,3]
# # Entrada: ([1,2,3,4,5], 1)
# Saída: [5,1,2,3,4]

def rotacionar(lista, k):
    while k > 0:
        i = 0
        temp = lista[i+1]
        while i < len(lista) - 1:
            if i == 0:
                lista[i+1] = lista[i]
                lista[i] = lista[-1]
            else:
                next_temp = lista[i+1]
                lista[i+1] = temp
                temp = next_temp


            i += 1
        k -= 1
    return lista

result = rotacionar([1,2,3,4,5], 2)
print(result)