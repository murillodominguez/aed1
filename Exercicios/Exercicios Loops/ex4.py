#4- Conte quantos números de 1 a 1000 são divisíveis por 7.
cont = 0

i = 1

while i <= 1000:
    if i % 7 == 0:
        cont += 1
    i += 1

print(f"{cont} números de 1 a 1000 são divisíveis por 7.")