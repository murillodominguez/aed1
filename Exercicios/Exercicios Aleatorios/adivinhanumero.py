import random

START = 1
END = 100
n = random.randint(START, END)
secret = "LOVE"
chances = 10
print(f"Tente adivinhar o número de {START} a {END} que eu pensei!\nVocê tem {chances} tentativas!")
guess = input("Digite seu palpite: ")
if guess == secret:
    print("Uau, um easter egg!")
else:
    while (guess != n or guess != secret) and chances >= 1:
        guess = input("Digite seu palpite: ")
        if guess != secret:
            guess = int(guess)
            chances -= 1
            if chances > 0:
                if guess < START or guess > END:
                    print(f"Puta merda bixo, eu te falei que era de {START} a {END}. ANIMAL! Tenta de novo.")
                else:
                    print(f"Nossa. Que horrível cara, tenta de novo!\n")
                if guess > n:
                    print(f"DICA: O número é menor.\n")
                else:
                    print(f"DICA: O número é maior.\n")
                print(f"Você ainda tem {chances} tentativas!\n\n")

    if n == guess:
        print(f"Uau! Você adivinhou, era realmente {n}!")
    if n == secret:
        print("Uau, um easter egg!")
    else:
        print("Game Over!")