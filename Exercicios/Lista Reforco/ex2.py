# 2- Implemente um programa que recebe uma string e um número N e desloca cada letra do texto N posições no alfabeto
# (ex: "abc", 2 → "cde"). Se passar do "z", deve voltar para o "a”.

string = input('Digite uma string: ')

n = int(input('Digite quanto cada letra vai caminhar no alfabeto: '))

output_string = ''
i = 0
for letter in string:
    char_code = ord(letter)
    substitute_char = letter
    if char_code >= 65 and char_code <= 90 or char_code >= 97 and char_code <= 122:
        next_letter_code = char_code + n
        if char_code <= 90:
            if next_letter_code > 90:
                next_letter_code = next_letter_code % 91 + 65
        else:
            if next_letter_code > 122:
                next_letter_code = next_letter_code % 123 + 97
        substitute_char = chr(next_letter_code)
    
    output_string += substitute_char
    i += 1

print(output_string)