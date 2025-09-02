# 1- Dada uma lista de strings, crie um programa que retorne apenas as que são palíndromos (iguais de frente pra trás).
string_input = ''
string_list = []
output_list = []
while string_input != '0':
    string_input = input("Informe uma string (Digite 0 para parar de inserir): ")
    if string_input != '0':
        string_input = string_input.upper()
        string_list.append(string_input)

for word in string_list:
    reversed_word = ''
    i = len(word) - 1
    while i >= 0:
        reversed_word += word[i]
        i -= 1
    print(reversed_word)
    if reversed_word == word:
        output_list.append(reversed_word)

print(output_list)
        
