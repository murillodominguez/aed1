list_num = []

num = None

while num != "":
    try:
        num = input("Digite um número inteiro (vazio para parar): ")
        if num != "":
            num = int(num)
            list_num.append(num)

    except ValueError:
        print("Informe um número inteiro.")

    except KeyboardInterrupt:
        print("\nPrograma encerrado.")
        num = ""

positive_num = []
negative_num = []

for num in list_num:
    if num >= 0:
        positive_num.append(num)
    else:
        negative_num.append(num)

print(f'LISTA DE TODOS NUMEROS: {list_num}\n\nLISTA POSITIVOS: {positive_num}\n\nLISTA NEGATIVOS: {negative_num}')