#2. Estatísticas de Texto
# Crie uma função `estatisticas_texto(texto)` que receba uma string e retorne uma lista com:
# - número de palavras,
# - número de caracteres,
# - tamanho médio das palavras,
# - a palavra mais longa.
# Exemplo:
# Entrada: "Python é divertido"
# Saída:
# [['palavras', 'caracteres', 'tamanho_medio', 'mais_longa'], [3, 17, 5.6, 'divertido'}]]

def estatisticas_texto(texto):
    lista = []
    word_counter = 0
    biggest_word_len = 0
    biggest_word = ''
    temp_word = ''
    word_counter = 1
    char_counter = 0
    letter_counter = 0
    word_len_counter = 0
    last_char = ''

    if len(texto) == 0:
        word_counter = 0

    i = 0
    for char in texto:
        if i > 0:
            last_char = texto[i-1]
        char_counter += 1
        if last_char == ' ':
            print(temp_word)
            if len(temp_word) > biggest_word_len:
                biggest_word = temp_word
                biggest_word_len = word_len_counter
            word_len_counter = 0
            temp_word = ''
            word_counter +=1
        if char != ' ':
            temp_word += char
            word_len_counter += 1
            letter_counter += 1
            if i == len(texto) - 1:
                if len(temp_word) > biggest_word_len:
                    biggest_word = temp_word
                    biggest_word_len = word_len_counter
                word_len_counter = 0
                temp_word = ''
        i += 1

    medium_len = letter_counter / word_counter
    lista += [['palavras', 'caracteres', 'tamanho_medio', 'mais_longa'],[word_counter, char_counter, medium_len, biggest_word]]
    return lista

estatistica = estatisticas_texto('Aqui eu sou o cara mais feliz do mundoooo')
print(estatistica)