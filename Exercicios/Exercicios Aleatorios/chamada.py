def chamada(nome, lista):
  if nome in lista:
    return lista
  lista.append(nome)
  return lista

lista = ["Guilherme", "Juan", "Breno", "José", "Eduardo"]

nome = input("Insira um nome: ")
print(chamada(nome,lista))