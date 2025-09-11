#Dada uma lista de palavras, agrupe as que são anagramas (mesmas letras em ordem diferente).
# Exemplo:

#Entrada →["amor", "roma", "carro", "roca", "arco"]

#Saída →[["amor", "roma"], ["carro"], ["roca", "arco"]]

string_input = ''
string_list = ["amor", "roma", "arrco", "carro", "roca", "arco", "maro", "abcd"]
output_list = []

# while string_input != '0':
#     string_input = input('Digite uma string (Digite 0 para parar): ')
#     if string_input != 0:
#         string_list.append(string_input)

normalized_string_list = []

for word in string_list:
    normalized_word = word.upper()
    normalized_string_list.append(normalized_word)

i = 0
while i < len(string_list):
    word = normalized_string_list[i]
    list_element = [string_list[i]]
    j = 0
    while j < len(string_list):
        char_vector = [
            0,0,0,0,0,0,
            0,0,0,0,0,0,
            0,0,0,0,0,0,
            0,0,0,0,0,0,0,0
        ]
        if j != i:
            comp_word = normalized_string_list[j]
            print(word,comp_word)
            if len(comp_word) == len(word):
                k = 0
                while k < len(word):
                    char_position1 = ord(word[k]) - 65
                    char_position2 = ord(comp_word[k]) - 65
                    print(word[k], comp_word[k])
                    
                    char_vector[char_position1] += 1
                    char_vector[char_position2] -= 1
                    k += 1
                if char_vector == [
                0,0,0,0,0,0,
                0,0,0,0,0,0,
                0,0,0,0,0,0,
                0,0,0,0,0,0,0,0
                ]:
                    list_element.append(string_list[j])
        j += 1
    print(list_element)
    output_list.append(list_element)
    i += 1

i = 0
while i < len(output_list):
    list_item = output_list[i]
    if len(list_item) > 1:
        j = 0
        while j < len(output_list):
            if j != i:
                item = output_list[j]
                reverse_item = []
                l = len(item) - 1
                while l >= 0:
                    reverse_item.append(item[l])
                    l -= 1
                if list_item == reverse_item:
                    output_list.pop(j)
            j += 1
    i += 1

print(output_list)