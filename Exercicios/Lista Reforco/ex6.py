#6- Faça um sistema de votação. O programa deve:

# - Pedir votos (número do candidato) em loop até digitar "fim"
# - Mostrar o candidato vencedor (ou empate) ao final

vote = ''
candidatos = []
contagem_votos = []
while vote != 'fim':
  vote = input('Digite um número de candidato para votar: ')
  if vote != 'fim':
    if vote not in candidatos:
      candidatos.append(vote)
      contagem_votos.append(0)
    if vote in candidatos:
      i = 0
      while i < len(candidatos):
        if vote == candidatos[i]:
            contagem_votos[i] += 1
        i += 1



print('=== SISTEMA DE VOTOS ===\n')
i = 0
maior_n_votos = 0
mais_votados = []
while i < len(candidatos):
  candidato = candidatos[i]
  votos = contagem_votos[i]
  if votos > maior_n_votos:
    maior_n_votos = votos
    mais_votado = [candidato]
  if votos == maior_n_votos:
    mais_votados.append(candidato)
  i += 1

resultado = ''

if len(mais_votados) > 1:
  concat_candidatos = ''

  i = 0
  while i < len(mais_votados):
    candidato = mais_votados[i]
    if i == len(mais_votados) - 2:
      concat_candidatos += candidato + ' e '
    else:
      concat_candidatos += candidato + ', '
    i += 1

  concat_candidatos = concat_candidatos.rstrip(', ')
  resultado = f'Houve um empate! Os candidatos {concat_candidatos} empataram com {maior_n_votos} votos.'
else:
  resultado = f'O candidato {mais_votados[0]} venceu com {maior_n_votos} votos.'

i = 0

for candidato in candidatos:
  print(f'Candidato {candidato}: {contagem_votos[i]} votos')
  i += 1
print('\n'+resultado)