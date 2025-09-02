#5 Leia nome completo e o pronome de tratamento e mostre Pronome Sobrenome, Nome
nome_completo = input("Informe nome completo no formato 'NOME SOBRENOME': ")
sobrenome = ""
nome = ""
pronome = input("Informe seu pronome de tratamento: ")
i = 0
space = 0
while i < len(nome_completo):
    if space > 0:
        sobrenome += nome_completo[i]
    else:
        if nome_completo[i] == " ":
            space += 1
        nome += nome_completo[i]
    i += 1

nome_f = f"{pronome} {sobrenome}, {nome}"    
print(nome_f)