#4 Leia uma palavra e mostre ela nesse cenário: Cada consoante é trocada pela próxima consoante do alfabeto
#Cada vogal foi trocada pelo n° correspondente sendo A=1 E=2 I=3 O=4 U=5

# palavra = input("Insira uma palavra: ").lower()
# i = 0
# novapalavra = ""
# while i < len(palavra):
#     if palavra[i] == "a":
#         novapalavra += "1"
#     if palavra[i] == "b":
#         novapalavra += "c"
#     if palavra[i] == "c":
#         novapalavra += "d"
#     if palavra[i] == "d":
#         novapalavra += "f"
#     if palavra[i] == "e":
#         novapalavra += "2"
#     if palavra[i] == "f":
#         novapalavra += "g"
#     if palavra[i] == "g":
#         novapalavra += "h"
#     if palavra[i] == "h":
#         novapalavra += "j"
#     if palavra[i] == "i":
#         novapalavra += "3"
#     if palavra[i] == "j":
#         novapalavra += "k"
#     if palavra[i] == "k":
#         novapalavra += "l"
#     if palavra[i] == "l":
#         novapalavra += "m"
#     if palavra[i] == "m":
#         novapalavra += "n"
#     if palavra[i] == "n":
#         novapalavra += "p"
#     if palavra[i] == "o":
#         novapalavra += "4"
#     if palavra[i] == "p":
#         novapalavra += "q"
#     if palavra[i] == "q":
#         novapalavra += "r"
#     if palavra[i] == "r":
#         novapalavra += "s"
#     if palavra[i] == "s":
#         novapalavra += "t"
#     if palavra[i] == "t":
#         novapalavra += "v"
#     if palavra[i] == "u":
#         novapalavra += "5"
#     if palavra[i] == "v":
#         novapalavra += "w"
#     if palavra[i] == "w":
#         novapalavra += "x"
#     if palavra[i] == "x":
#         novapalavra += "y"
#     if palavra[i] == "y":
#         novapalavra += "z"
#     if palavra[i] == "z":
#         novapalavra += "b"
#     i += 1
# print(novapalavra)
#îîî MODO BURRO

palavra = input("Insira uma palavra: ")
palavra = palavra.lower()
palavra_nova = ""
consoantes = "bcdfghjklmnpqrstvwxyz"
vogais = "aeiou"

i = 0
while i < len(palavra):
    j = 0
    while j < len(consoantes):
        if palavra[i] == consoantes[j]:
            if consoantes[j] == "z":
                palavra_nova += "b"
            else:
                palavra_nova += consoantes[j+1]
        j += 1
    j = 0
    while j < len(vogais):
        if palavra[i] == vogais[j]:
            palavra_nova += str(j+1)
        j += 1
    i += 1

print(palavra_nova)