# 5. Ordenação de Palavras por Critério Personalizado
# Escreva uma função `ordenar_palavras(frase)` que:
# 1. Separe a frase em palavras,
# 2. Ordene as palavras primeiro pelo tamanho e depois em ordem alfabética.
# Exemplo:
# Entrada: "banana uva abacaxi pera morango"
# Saída: ["uva", "pera", "banana", "morango", "abacaxi"]

def custom_split(frase):
    words = []
    temp = ''
    for char in frase:
        if char == ' ':
            words += [temp]
            temp = ''
        else:
            temp += char
    words += [temp]

    return words

def order_len(words):
    i = 0
    while i < len(words):
        j = i+1
        while j < len(words):
            if len(words[i]) > len(words[j]):
                temp = words[i]
                words[i] = words[j]
                words[j] = temp
            j += 1
        i += 1
    return words

def sort_alphabetic(words):
    i = 0
    while i < len(words):
        j = 0
        while j < len(words):
            if len(words[i]) == len(words[j]):
                k = 0
                while k < len(words[i]):
                    if words[i][k] > words[j][k]:
                        temp = words[i]
                        words[i] = words[j]
                        words[j] = temp
                        break
                    k += 1
            j += 1
        i += 1
    return words
        



def ordenar_palavras(frase):
    words = custom_split(frase)
    words = order_len(words)
    words = sort_alphabetic(words)
    return words

frase = 'banana uva abacaxi pera morango'
words = ['banana', 'uva', 'abacaxi', 'pera', 'morango']
result = ordenar_palavras(frase)
print(result)

def bubble_sort(lista):
    i = 0
    while i < len(lista):
        j = i + 1
        while j < len(lista):
            if lista[i] > lista[j]:
                temp = lista[i]
                lista[i] = lista[j]
                lista[j] = temp
            j += 1
        i += 1
    return lista