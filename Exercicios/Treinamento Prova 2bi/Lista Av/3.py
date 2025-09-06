# 3. Codificação Cíclica (Cifra de César)
# Escreva uma função `cifra_cesar(texto, k)` que receba uma string e um número inteiro `k`.
# - Cada letra deve ser deslocada `k` posições no alfabeto (circular).
# - Não altere espaços nem pontuação.
# - Aceite tanto maiúsculas quanto minúsculas.
# Exemplo:
# Entrada: ("Abacaxi", 3)
# Saída: "Dedfdal

def cifra_cesar(string, k):
    cifrada = ''

    for char in string:
        char_code = ord(char)
        new_char_code = char_code + k

        if char_code >= 65 and char_code <= 122 and (char_code <= 90 or char_code >= 97):
            if char_code <= 90:
                print(new_char_code)
                while new_char_code > 90:
                    new_char_code -= 91
                    new_char_code += 65

            else:
                if new_char_code > 122:
                    print(new_char_code)
                    while new_char_code > 122:
                        new_char_code -= 123
                        new_char_code += 97
            cifrada += chr(new_char_code)
        else:
            cifrada += char
    return cifrada
            
            
cifra = cifra_cesar('Abacaxi', 3)

print(cifra)