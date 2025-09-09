# 18. Combinações de Pares
# Crie uma função `pares(lista)` que receba uma lista de números e retorne uma lista com
# todos os pares possíveis (sem repetição).
# Exemplo:
# Entrada: [1,2,3]
# Saída: [(1,2),(1,3),(2,3)]

def pares(lista):
	i = 0
	pares = []
	while i < len(lista):
		j = 0
		while j < len(lista):
			if j != i:
				par = [lista[i], lista[j]]
				pares.append(par)
			j += 1
		i += 1
	return pares

pares = pares([1,1,1])

print(pares)

def geraanagramas(p):
	i = 0
	p = list(p)
	print(p)
	pares = []
	while i < len(p):
		j = 0
		par = [p[i]]
		while j < len(p):
			if j != i:
				par.append(p[j])
			j += 1
		pares.append("".join(par))
		i += 1
	return pares

palindromos = geraanagramas('abc')
print(palindromos)