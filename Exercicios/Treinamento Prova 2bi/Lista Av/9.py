# 9. Contador de Vogais Únicas
# Escreva uma função `vogais_unicas(texto)` que conte quantas vogais distintas aparecem na
# string.
# Exemplo:
# Entrada: "Programacao"
# Saída: 3

def vogais_unicas(texto):
    vowels_found = []
    vowels = 'aeiouAEIOU'
    for letra in texto:
        if letra in vowels and letra.lower() not in vowels_found:
            vowels_found.append(letra.lower())
    return len(vowels_found)

print(vogais_unicas("Programacao"))  # Saída: 3