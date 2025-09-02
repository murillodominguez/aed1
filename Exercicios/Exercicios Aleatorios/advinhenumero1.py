import random

START = 1
END = 100
n = random.randint(START, END)
secret = "LOVE"
chances = 10
won = False

print(f"Tente adivinhar o número de {START} a {END} que eu pensei!\nVocê tem {chances} tentativas!")

while chances > 0 and not won:
    guess = input("Digite seu palpite: ")
    chances -= 1
    if guess == secret:
        print("Uau, um easter egg! Você ganhou então, eu acho... (Que sem graça...)")
        won = True
    else:
        if guess.isdigit():
            guess = int(guess)
            if guess == n:
                print(f"Uau! Você adivinhou, era realmente {n}! Parabéns!")
                won = True
            else:
                if chances > 0:
                    if guess < START or guess > END:
                        print(f"Puta merda bixo, eu te falei que era de {START} a {END}. ANIMAL! Tenta de novo.")
                    else:
                        print(f"Nossa. Que horrível cara, tenta de novo!\n")
                    if guess > n:
                        print(f"DICA: O número é menor.\n")
                    else:
                        print(f"DICA: O número é maior.\n")
        else:
            print("Ei! Aqui aceitamos apenas números! A não ser que tu queiras forçar o sistema...")
    if not won:
        if chances > 0:
            print(f"Você ainda tem {chances} tentativa(s)!\n\n")
        else:
            print(f"Game Over! O número era {n}.")
