# 10. Compactação de Strings (Run-Length Encoding)
# Implemente uma função `compactar(texto)` que comprima a string substituindo sequências
# de caracteres repetidos pelo caractere seguido da contagem.
# Depois, implemente `descompactar(texto)` que faça o processo inverso.
# Exemplo:
# Entrada: "aaabbcccc"
# Saída: "a3b2c4"

def compactar(texto):
    i = 0
    compacted = ''
    last_char = ''
    c = 1

    while i < len(texto):
        if texto[i] == last_char:
            c += 1
        else:
            if c > 1:
                compacted += str(c)
                c = 1
            compacted += texto[i]
        last_char = texto[i]
        i += 1
    if c > 1:
        compacted += str(c)

    return compacted

compacted = compactar("aaabbcccc")
print(compacted)  # Saída: "a3b2c4"