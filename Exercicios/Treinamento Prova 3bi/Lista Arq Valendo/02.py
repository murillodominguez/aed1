file1 = input("Digite o nome do primeiro arquivo: ")
file2 = input("Digite o nome do segundo arquivo: ")

try:
    with open(file1) as file:
        file1_txt = file.read()
    with open(file2) as file:
        file2_txt = file.read()

except FileExistsError:
    print('O arquivo informado não existe!')