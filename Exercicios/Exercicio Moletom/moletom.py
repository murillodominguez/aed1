nomes = []
tamanhos = []

nome = input('Nome: ')

while nome != "":
    tamanho = input('Tamanho: ').upper()
    print(tamanho, nome)
    if tamanho == "PP" or tamanho == "P" or tamanho == "M" or tamanho == "G" or tamanho == "GG":
        nomes.append(nome)
        tamanhos.append(tamanho)
        nome = input('Nome: ')
    else:
        print('Tamanho inválido!')

list_size = len(nomes)

VALOR_MOLETOM = 135
valor_total = 0
i = 0

while i < list_size:
    valor_total += VALOR_MOLETOM
    i += 1

print('FECHOU. LISTA POPULADA\n')

select_tam = input('Escreva o tamanho que você deseja contar quantos foram comprados (PP, P, M ou G): ').upper()
i = 0
cont_tam = 0

while i < list_size:
    if tamanhos[i] == select_tam:
        cont_tam += 1
    i += 1

select_name = input('Escreva um nome para descobrir o tamanho do moletom da pessoa: ').upper()
i = 0
name_in_list = False

while i < list_size:
    if nomes[i].upper() == select_name:
        name_in_list = True
        select_name = nomes[i]
        tam_of_person = tamanhos[i]
    i += 1

tam_search_parameter = input('Informe um tamanho para pesquisar quem encomendou ele: ').upper()
i = 0
list_encomendaram = []
while i < list_size:
    if tamanhos[i] == tam_search_parameter:
        list_encomendaram.append(nomes[i])
    i += 1

if name_in_list:
    print(f'Tamanho encomendado por {select_name}: {tam_of_person}')
else:
    print(f'Nome "{select_name}" não encontrado!')
print(f'Lista de quem comprou moletom e seus respectivos tamanhos: ')

i = 0
for nome in nomes:
    print(f"{nome}, tamanho {tamanhos[i]}")
    i += 1
if len(list_encomendaram):
    print(f'\nLista de quem comprou o tamanho {tam_search_parameter}: ')
    for cliente in list_encomendaram:
        print(cliente)
else:
    print(f"Ninguém comprou moletom do tamanho {tam_search_parameter}")
if cont_tam == 0:
    print(f'\nNão foram comprados moletons do tamanho {select_tam}')
else:
    print(f'\nForam comprados {cont_tam} moletons do tamanho {select_tam}')
print(f'\nValor total: {valor_total}')


html = "<html><head><meta charset=UTF-8></head><body>"
html += "<h1 align='center'>Visão Geral da Compra dos Moletons</h1>"
html += "<table align='center' border=1 width=500 height=200>"
html += "<tr><td align='center'>Nome</td><td align='center'>Tamanho</td><td align='center'>Total a arrecadar</td></tr>"
i = 0
while i < list_size:
    html += "<tr>"
    j = 0
    while j < 2:
        if j == 0:
            html += f"<td align='center'>{nomes[i]}</td>"
        if j == 1:
            html += f"<td align='center'>{tamanhos[i]}</td>"
        j += 1
    if i == 0:
        html += f"<td rowspan={list_size} align='center'>R${valor_total}</td>"
    html += "</tr>"
    i += 1
html += "</table></body></html>"

print(f'\n\n\n{html}')
with open("tabela_moletom.html", "w") as file:
    file.write(html)