def find_in_lists(lista, index):
    flattened_list = flatten_list(lista)
    if index > len(flattened_list) - 1:
        return 'ERRO'
    
    acesso = '['

    element = flattened_list[index]
    for i, item in enumerate(lista):
        if element in item:
            acesso += str(i) + ','
            if isinstance(item, list):
                for j, subitem in enumerate(item):
                    if subitem == element:
                        acesso += str(j) + ']'

    return acesso


def flatten_list(lista):
    result = []
    for item in lista:
        if isinstance(item, list):
            result += flatten_list(item)
        else:
            result += item

    return result

lista = [['A','B'],['D'],['E','F','G','H'],['I','J','K'],['L','M','N','O']]

result = find_in_lists(lista, 10)

print(result)