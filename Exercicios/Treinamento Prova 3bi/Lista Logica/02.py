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
c_zeros = 0
c_positivos = 0
c_negativos = 0


for num in list_num:
    if num >= 0:
        positive_num.append(num)
        if num != 0:
            c_positivos += 1
    else:
        negative_num.append(num)
        c_negativos += 1

final_positive_num = []

for i, num in enumerate(positive_num):
    if num == 0:
        c_zeros += 1
    else:
        final_positive_num.append(num)



print(f'LISTA DE TODOS NUMEROS: {list_num}\n\nLISTA POSITIVOS: {final_positive_num}\n\nLISTA NEGATIVOS: {negative_num}\n\nTINHAM {c_zeros} NA LISTA DE POSITIVOS.\n\nEM POSITIVOS TEMOS {c_positivos} NÚMEROS E EM NEGATIVOS {c_negativos} NÚMEROS')