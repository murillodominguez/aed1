class ZeroElevadoAZero(Exception):
  pass

def potencia(base, exp):
  if base == 0:
    if exp == 0:
      raise ZeroElevadoAZero("ERRO: 0^0 é indeterminado na matemática. Informe outro valor.")
    return 0
  
  if exp == 0:
    return 1
  
  if exp == 1:
    return base

  result = base

  if exp < 0:
    abs_exp = exp * -1
    result = 1/base
    while abs_exp > 1:
      result = result * 1/base
      abs_exp -= 1

  while exp > 1:
    result = result * base
    exp -= 1
  
  return result

base = float(input('Informe a base da sua potenciação: '))
exp = float(input('Informe o expoente da potenciação: '))

try:
  resultado = potencia(base,exp)
  print(f'{base} ^ {exp} = {resultado}')
except ZeroElevadoAZero as e:
  print(e)