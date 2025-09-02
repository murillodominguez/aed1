#6- Peça para o usuário digitar frases até que ele digite a palavra “sair”. Diga quantas frases foram digitadas.
frase = ""
cont = 0

while frase != "sair":
    frase = input('Digite uma frase (digite "sair" para finalizar o programa ): ')
    if frase != "sair":
        cont += 1

print(f"O usuário informou {cont} frases.")