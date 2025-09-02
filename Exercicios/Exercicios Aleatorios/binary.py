def convert_to_bin(n):
  if n < 2:
    return str(n)
  return convert_to_bin(n//2) + str(n%2)

print(convert_to_bin(20))
'''def divide_by_2_i_times(n, i):
  while i > 0:
    n = n//2
    i -= 1
  return n

def count_exp(n):
  c = 0
  while n > 1:
    n = n // 2
    c += 1
  return c

def convert_to_bin(n):
  if n < 2:
    return n
  binary = ""
  #1111 -> 2^4
  n_exp = count_exp(n)
 
  while(n_exp >= 0):
    n_reversed = divide_by_2_i_times(n, n_exp)
    binary += str(n_reversed%2)
    n_exp -= 1
  return binary

print(convert_to_bin(16))'''