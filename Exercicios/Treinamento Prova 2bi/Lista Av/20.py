# 20. Produto Cartesiano
# Implemente `produto_cartesiano(lista1, lista2)` que retorne todas as combinações possíveis
# entre elementos de duas listas.
# Exemplo:
# Entrada: ([1,2], ['a','b'])
# Saída: [(1,'a'),(1,'b'),(2,'a'),(2,'b')]

def produto_cartesiano(lista1, lista2):
    produto = []
    i = 0
    while i < len(lista1):
        j = 0
        while j < len(lista2):
            row = [lista1[i], lista2[j]]
            produto.append(row)
            j += 1
        i += 1
    return produto

result = produto_cartesiano([1,2], ['a', 'b'])
print(result)