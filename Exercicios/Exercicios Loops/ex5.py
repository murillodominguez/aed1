#5- Peça uma frase e uma letra. Conte quantas vezes essa letra aparece na frase.
frase = input("Digite uma frase: ")
letra = input("Digite uma letra: ")
cont = 0

i = 0

while i < len(frase):
    if frase[i] == letra:
        cont +=1
    i += 1

print(f'A letra {letra} aparece {cont} vezes na frase "{frase}".')