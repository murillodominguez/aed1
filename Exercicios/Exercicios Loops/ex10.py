#10- Remova todos os espaços de uma frase lida.
str = input("Digite uma frase: ")
str_formatada = ""

i = 0

while i < len(str):
    char = str[i]
    if char != " ":
        str_formatada += char
    i += 1

print(str_formatada)