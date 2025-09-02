#2- Some números lidos até que a entrada seja zero. Se o resultado for um número ímpar, multiplique-o por 2.
n = 1
soma = 0

while n != 0:
    n = int(input("Informe um número (digite 0 para encerrar o programa): "))
    if n % 2 == 1:
        n *= 2
    soma += n

print(soma)