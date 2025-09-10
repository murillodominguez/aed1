#4- Peça uma senha e verifique se ela é válida segundo as regras:

#- Pelo menos 8 caracteres
#- Contém pelo menos uma letra maiúscula, uma minúscula e um número
#- Não pode ter espaços

senha = ''
while senha == '':
  senha = input('Digite uma senha: ')

if len(senha) < 8:
  print('SENHA INVÁLIDA:\nDeve ter no mínimo 8 caracteres')

else:
  check_capital_letters = False

  check_small_letters = False

  check_no_spaces = True

  for char in senha:
    char_code = ord(char)

    if char_code >= 65 and char_code <= 90:
      check_capital_letters = True
    if char_code >= 97 and char_code <= 122:
      check_small_letters = True
    if char_code == 32:
      check_no_spaces = False

  error = False
  error_msg = "SENHA INVÁLIDA:"

  if not check_capital_letters:
    error = True
    error_msg += "\nDeve ter no mínimo uma letra maiúscula" 

  if not check_small_letters:
    error_msg += "\nDeve ter no minímo uma letra minúscula"
    error = True

  if not check_no_spaces:
    error_msg += "\nNão pode ter espaços"
    error = True

  if not error:
    print('Senha válida!')
  else:
    print(error_msg)