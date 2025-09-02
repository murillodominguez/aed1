#3- Conte quantas vogais há em uma palavra.
palavra = input("Digite uma palavra para contar as vogais: ")
vogais = "aeiouAEIOUáéíóúÁÉÍÓÚâêôÂÊÔãõÃÕ"
cont = 0

i = 0

while i < len(palavra):
    j = 0
    while j < len(vogais):
        if palavra[i] == vogais[j]:
            cont += 1
        j += 1
    i += 1

if cont == 0:
    print("Essa palavra não tem vogais. VAI ESCREVER EM PORTUGUÊS!")
else:
    print(f'A palavra "{palavra}" tem {cont} vogais.')