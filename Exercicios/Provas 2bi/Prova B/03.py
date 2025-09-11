def normaliza(txt):
    not_allowed = ',- '
    normalized = ''
    not_allowed_count = 0

    for char in txt:
        if char in not_allowed:
            not_allowed_count += 1
            if len(normalized) > 0 and not_allowed_count == 1:
                normalized += ' '
        else:
            not_allowed_count = 0
            normalized += char

    normalized = normalized.split(' ')
    
    result = ''

    tam = len(normalized)
    i = 0
    while i < tam:
        word = normalized[i]
        if i == tam - 2:
            result += word + ' e '
        elif i == tam - 1:
            result += word
        else:
            result += word + ', '
        i += 1

    return result

txt = 'maçã,banana--pêra melão        melancia'

print(normaliza(txt))