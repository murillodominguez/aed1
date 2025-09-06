# 4. Substring Única
# Implemente uma função `maior_substring_unica(texto)` que encontre a maior substring sem
# caracteres repetidos.
# Exemplo:
# Entrada: "abcabcbb"
# Saída: "abc"
# Entrada: "bbbbb"
# Saída: "b"

def maior_substring_unica(texto):
    substring_temp = ''
    maior_substring_len = 0
    maior_substring = ''
    for char in texto:
        if len(substring_temp) > maior_substring_len:
            maior_substring_len = len(substring_temp)
            maior_substring = substring_temp
        if char in substring_temp:
            substring_temp = ''
        substring_temp += char

    return maior_substring

maior_substring = maior_substring_unica('bbbbb')

print(maior_substring)