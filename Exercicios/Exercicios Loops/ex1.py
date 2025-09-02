#1- Conte quantos caracteres tem uma palavra lida.
palavra = input("Digite uma palavra: ")
palavra_aux = palavra
i = 0

while palavra_aux != "":
    i += 1
    palavra_aux = palavra_aux[1:]

print(f'A palavra "{palavra}" tem {i} caracteres.')