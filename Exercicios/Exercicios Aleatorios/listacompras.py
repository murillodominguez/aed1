lista = []

item = input("Novo item (espaço em branco para finalizar compra): ")

while item != "":
    lista.append(item)
    item = input("Novo item (espaço em branco para finalizar compra): ")
    
i = 0
while i < len(lista):
    print(lista[i])
    i += 1