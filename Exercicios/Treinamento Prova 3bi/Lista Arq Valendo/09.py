# import os
# SOLUÇÃO BARBADA
# cwd = os.getcwd()

# print(cwd)

# with open('pares.txt') as file:
#     pares = file.readlines()
#     pares = [int(p.strip()) for p in pares]

# with open('impares.txt') as file:
#     impares = file.readlines()
#     impares = [int(i.strip()) for i in impares]

# numbers = pares + impares

# numbers = sorted(numbers)

# with open('pareseimpares.txt', 'w') as file:
#     for number in numbers:
#         file.write(f"{number}\n")

#SOLUÇÃO HARD

with open('pares.txt') as even_file:
    with open('impares.txt') as odd_file:
        i = 0
        while i < len(even_file.readlines()) or i < len(odd_file.readlines()):
            even_file.seek(0)
            odd_file.seek(0)
            even_lines = even_file.readlines()
            odd_lines = odd_file.readlines()
            if i < len(even_lines):
                with open('pareseimpares.txt', 'a') as output_file:
                    output_file.write(even_lines[i])
            if i < len(odd_lines):
                with open('pareseimpares.txt', 'a') as output_file:
                    output_file.write(odd_lines[i])
            i += 1