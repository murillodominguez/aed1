#9- Verifique se uma string é formada apenas por letras.
string = input("Digite uma string: ")
normalized_string = string.lower()
letras = "abcdefghijklmnopqrstuvwxyzáéíóúâêîôûãẽĩõũàèìòù"
only_letters = True

i = 0

while i < len(string):
    j = 0
    is_letter = False

    while j < len(letras):

        if normalized_string[i] == letras[j]:
            is_letter = True
        j += 1

    if not is_letter:
        only_letters = False
    i += 1

if only_letters and not string == "":
    print(f"A string ( {string} ) é formada apenas por letras.")
else:
    print(f"A string ( {string} ) não é formada apenas por letras.")