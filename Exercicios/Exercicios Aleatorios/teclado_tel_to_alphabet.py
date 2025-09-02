# Traduzir um código de teclado de telefone antigo. EX: 22 = 'b', 33 = 'e', 2 = 'a'

def translate_nokia_alphabet(code):
  keyboard = [['0', '2', '22', '222', 
              '3', '33', '333',
              '4', '44', '444',
              '5', '55', '555',
              '6', '66', '666',
              '7', '77', '777', '7777',
              '8', '88', '888',
              '9', '99', '999', '9999'],
              [' ', 'a', 'b', 'c', 'd', 'e',
               'f', 'g', 'h', 'i', 'j',
               'k', 'l', 'm', 'n', 'o',
               'p', 'q', 'r', 's', 't',
               'u', 'v', 'w', 'x', 'y', 'z']]
  text = ''
  digit = code[0]

  for i in range(1, len(code)):
    if code[i] == digit[-1]:
      digit += code[i]
    else:
      for j in range(len(keyboard[0])):
        if digit == keyboard[0][j]:
          text += keyboard[1][j]
      digit = code[i]
  for j in range(len(keyboard[0])):
    if digit == keyboard[0][j]:
      text += keyboard[1][j]

  return text
print(translate_nokia_alphabet('6664033'))