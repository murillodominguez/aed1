#7- Mantenha duas listas: produtos e quantidades.

#- O programa deve permitir adicionar produto, remover e vender (diminuindo quantidade).
#- Se um produto esgotar, deve removê-lo das listas.

resposta = ''
produtos = []
quantidades = []

while resposta != 'fim':
  lista_produtos = ''
  if len(produtos) > 0:
    lista_produtos = "=== LISTA DE PRODUTOS ===\n"
    for produto in produtos:
      lista_produtos += f'{produto}\n'

  resposta = input('O que você deseja fazer? (1 - ADICIONAR 2- REMOVER 3- VENDER "fim"- ENCERRAR PROGRAMA): ').lower()
  
  if resposta == '1':
    tentativa = 'sim'
    while tentativa == 'sim':
      produto = input('Digite o nome do produto a inserir:')
      if produto in produtos:
        print(f'O produto "{produto}" já está cadastrado!')
      else:
        produtos.append(produto)
        print(f'Produto "{produto}" adicionado com sucesso!')
      tentativa = input('Deseja adicionar outro produto? (SIM ou NÃO)').lower()

  if resposta == '2':
    if len(lista_produtos) > 1:
      print(lista_produtos)
      produto = input('Digite o nome do item que você deseja remover: ').lower()
      if produto not in produtos:
        print(f'O produto "{produto}" não existe!')
      else:
        produtos.remove(produto)
    else:
      print('Não há itens na lista de produtos!')
    
    
