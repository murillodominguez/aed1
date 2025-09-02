tijolo = input("Digite o caractere para ser tijolo da sua pirâmide: ")
altura = int(input("Digite a altura da pirâmide: "))
piramide = ""

i = 0

#Versão Pythonística Nível de Abstração quebrando o céu
# while i < altura:
#     blank_space = " " * (altura - i)
#     piramide += blank_space + tijolo * (1 + i*2) + "\n"
#     i += 1

while i < altura:
    blank_space = altura - i
    bricks = 1 + i*2
    row_length = blank_space + bricks
    j = 0

    while j < row_length:
        if j < blank_space:
            piramide += " "
        else:
            piramide += tijolo
        j += 1
    piramide += "\n"
    i += 1

print(piramide)