# 14. Triângulo de Pascal
# https://pt.wikipedia.org/wiki/Tri%C3%A2ngulo_de_Pascal
# Crie uma função `triangulo_pascal(n)` que retorne uma lista de listas representando as
# primeiras `n` linhas do triângulo de Pascal.

def triangulo_pascal(n):
    i = 0
    result = []
    while i < n:
        row = []
        if i == 0:
            row += [1]
        if i == 1:
            row += [1, 1]
        if i > 1:
            j = 0
            while j <= i:
                if j == 0 or j == i:
                    row += [1]
                if j < i - 1:
                    row += [last_row[j] + last_row[j+1]]
                j += 1
        i += 1

        result.append(row)           
        last_row = row

    return result

result = triangulo_pascal(7)
print(result)


#versão recursiva

def recursive_pascal_triangle(n):
    if n == 1:
        return [[1]]
    triangle = recursive_pascal_triangle(n-1)
    last_row = triangle[-1]
    new_row = [1]
    i = 0
    while i < len(last_row) - 1:
        new_row.append(last_row[i] + last_row[i+1])
        i += 1
    new_row.append(1)
    triangle.append(new_row)
    return triangle

result = recursive_pascal_triangle(7)
print(result)