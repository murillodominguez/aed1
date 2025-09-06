#1. Palíndromos Recursivos

# Implemente uma função recursiva `eh_palindromo(texto)` que receba uma string e retorne
# `True` se for palíndromo (desconsiderando espaços, acentos e diferenças entre
# maiúsculas/minúsculas) e `False` caso contrário.
# Exemplo:
# Entrada: "Socorram-me subi no onibus em Marrocos"
# Saída: True

def eh_palindromo(texto):
    texto = format_string(texto)
    if len(texto) == 0:
        return True
    if texto[0] != texto[-1]:
        return False
    return eh_palindromo(texto[1:-1])

def format_string(texto):
    i = 0
    formatted_string = ''
    spaced_characters = [' ', '-']

    for letra in texto:
        if letra not in spaced_characters:
            formatted_string += letra.lower()
    
    return formatted_string

assertPalindromo = eh_palindromo('Socorram-me subi no onibus em Marrocos')

print(assertPalindromo)