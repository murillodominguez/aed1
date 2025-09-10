lifes = 6

palavra = 'morango'
encontradas = []
palpites = []
while lifes > 0:
    building_word = ''
    for i, item in enumerate(palavra):
        if palavra[i] in encontradas:
            building_word += palavra[i]
        else:
            building_word += '_'
    if building_word == palavra:
        print(f'VOCÊ GANHOU! a palavra era {palavra}')
        break
    print(f'Palavra = {building_word}\nVidas: {lifes}')
    if len(palpites) > 0:
        print(f'Letras que você já tentou: {palpites}')
    while True:
        palpite = input('\nDigite seu palpite: ')
        if palpite != '' and len(palpite) == 1:
            break
    if palpite not in palavra and palpite not in palpites:
        print('\nVocê errou! Imbecíl')
        lifes -= 1
    elif palpite in encontradas:
        print(f'\nVocê já tentou essa letra! Letras já usadas: {palpites}\n')
    else:
        encontradas += [palpite]
    if palpite not in palpites:
        palpites += [palpite]

if lifes == 0:
    print('Você perdeu seu imbéciL! Acabaram suas vidas. Hasta la vista')