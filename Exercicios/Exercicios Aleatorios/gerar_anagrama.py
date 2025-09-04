def fatorial(n):
  if n == 0:
    return 1

  return n * fatorial(n-1)

def gerar_anagrama(p, w = '', lista = []):
  print(lista)
  if len(lista) == fatorial(len(p)):
    print('hello')
    return lista
  if len(w) == len(p) and w not in lista:
    lista.append(w)
    for x in range(len(p)):
      gerar_anagrama(p, p[x], lista)
  for i in p:
    if i not in w:
      return gerar_anagrama(p, w+i, lista)
  
  # i = 0
  # while i < tam:
  #   w += p[i]
  #   j = 0
  #   while j < tam:
  #     if j != i:
  #       w += p[j]
  #     j += 1
  #   i += 1
  #   if len(w) == tam:
  #     lista.append(w)
  #     w = ''
matriz = gerar_anagrama('rabo')
print(matriz)
#string = 'boa'
# i = 0: string = 'b', string = 'o', string = 'a' -> j ---> list -> [b, o, a], list[i] += list[j] -> list = [bo, ba]
# i = 1: string = 'bo'+a, string = 'oa'+b string = 'ao'+b
# i = 2: string = 'boa', string = 'oba', string = 'abo'
# falta -> bao

# string[i] 

#string = 'rabo'
# i = 0: string = 'r', 'a', 'b', 'o' -> j
# i = 1: string = 'ra'+bo, 'ab'+or, 'bo'+ra
# i = 2: string = 'rab'+o, 'abo'+r
# i = 3: string = 'rabo', 'arbo', 'brao', 'orab'

