import random as rd

jogador1 = input("Digite o seu nome, player: ")
vitoria1 = (f"O jogador {jogador1} venceu!")
vitoria2 = (f"COM venceu!")
print("Pedra... Papel... Tesoouuu-ra!")

jogadap1 = input(f"Digite a jogada do jogador {jogador1}: ").lower()
jogadaCOM = rd.randint(0,2)
if jogadaCOM == 0:
	jogadaCOM = "pedra"
else:
	if jogadaCOM == 1:
		jogadaCOM = "papel"
	else:
		jogadaCOM = "tesoura"

if (jogadap1 != "pedra" and jogadap1 != "papel" and jogadap1 != "tesoura"):
	print("Erro! Jogada inválida.")

else:
	print("JOGADA DO BOT: " + jogadaCOM)
	if jogadap1 == jogadaCOM:
		print("Temos um empate!")
		
	else:
		if jogadap1 == "pedra":
			if jogadaCOM == "papel":
				print(vitoria2)
			else:
				print(vitoria1)

		if jogadap1 == "papel":
			if(jogadaCOM == "pedra"):
				print(vitoria1)
			else:
				print(vitoria2)

		if jogadap1 == "tesoura":
			if jogadaCOM == "pedra":
				print(vitoria2)
			else:
				print(vitoria1)
