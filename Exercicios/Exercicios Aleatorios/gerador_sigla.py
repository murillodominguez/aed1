def sigla_simples(word):
    sigla = word[0]
    for i in range(1, len(word)):
        if word[i-1] == ' ':
            sigla += word[i]           
    return sigla

# Centro de Ciências Computacionais

def siglaSplit(word):
    sigla = ''
    word = word.upper()
    words = word.split()
    last_initial = words[0][0]
    undesired_words = ['DA', 'DO', 'DE', 'DOS', 'DAS', 'PARA', 'E']
    c = 1
    i = 0
    for word in words:
        if word not in undesired_words:
            if word[0] == last_initial and i > 0:
                c += 1
            else:
                if c > 1:
                    sigla += str(c)  
                sigla += word[0]
                c = 1
            last_initial = word[0]
        i += 1

    if c > 1:
        sigla += str(c)

    return sigla
# No python ao invés de usar uma variável para salvar o último valor para selecionar o valor anterior
# Dá para selecionar a o último index do que está sendo concatenado (ex: saida[-1])
print(siglaSplit('Moletom Verde Vermelho É De Cor Caramela'))