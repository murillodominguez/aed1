# 5- Dada uma string, compacte-a substituindo sequências repetidas pela letra seguida da quantidade.

#Exemplo: "aaabbccccd" → "a3b2c4d1"

string = ''
compacted_string = ''

while string == '':
  string = input('Informe uma string: ')

last_char = string[0]
c = 0

for char in string:
  if char == last_char:
    if c == 0:
      compacted_string += char
    c += 1
  else:
    if c > 1:
      compacted_string += str(c)
    compacted_string += char
    c = 1
  last_char = char

if c > 1:
  compacted_string += str(c)

print(compacted_string)