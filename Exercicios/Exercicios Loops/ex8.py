#8- Leia uma frase e imprima ela ao contrario.
frase = input("Informe uma frase: ")
inverso = ""

i = len(frase)-1

while i >= 0:
    inverso += frase[i]
    i -= 1

print(f'O inverso de "{frase}" é "{inverso}"')