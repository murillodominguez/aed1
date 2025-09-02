def is_anagram(txt1, txt2):
    txt1 = list(txt1)
    txt2 = list(txt2)
    if len(txt1) == len(txt2):
        for i in range(len(txt1)):
            if txt2[i] not in txt1:
                return False
        return True
    return False

# Não funciona î

def is_anagram_right(txt1, txt2):
    txt1 = txt1.upper()
    txt2 = txt2.upper()

    lista = [0, 0, 0, 0, 0, 0,
             0, 0, 0, 0, 0, 0, 
             0, 0, 0, 0, 0, 0, 
             0, 0, 0, 0, 0, 0, 0, 0]
    
    if len(txt1) != len(txt2):
        return False
    
    for letter in txt1:
        i = ord(letter) - 65
        lista[i] += 1

    for letter in txt2:
        i = ord(letter) - 65
        lista[i] -= 1

    for frequency in lista:
        if frequency != 0:
            return False

    return True    

print(is_anagram_right('romar', 'morra'))