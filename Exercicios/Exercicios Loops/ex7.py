#7- Leia um caractere e um número n. Mostre um quadrado nxn com o caractere lido.
char = input("Informe um caractere para desenhar um quadrado: ")
n = int(input("Informe o lado do quadrado: "))
quadrado = ""

i = 0

while i < n:
    j = 0
    while j < n:
        quadrado += char
        j += 1
    quadrado += "\n"
    i += 1

print(quadrado)