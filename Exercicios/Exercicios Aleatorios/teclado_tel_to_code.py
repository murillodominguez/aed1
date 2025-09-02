def translate_alphabet_to_nokia(phrase):
  phrase = phrase.lower()
  keyboard = ['abc', 'def', 'ghi', 'jkl',
              'mno', 'pqrs', 'tuv', 'wxyz']
  code = ''
  for i in range(len(phrase)):
    if phrase[i] == ' ':
      code += '0'
    else:
      for j in range(len(keyboard)):
        if phrase[i] in keyboard[j]:
          number = str(j+2)
          if phrase[i] == keyboard[j][0]:
            code += number
          elif phrase[i] == keyboard[j][1]:
            code += number * 2
          elif phrase[i] == keyboard[j][2]:
            code += number * 3
          elif phrase[i] == keyboard[j][3]:
            code += number * 4
  return code

phrase = input('Digite um texto: ')

print(f'\n{translate_alphabet_to_nokia(phrase)}')