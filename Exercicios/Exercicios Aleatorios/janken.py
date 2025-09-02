jogador1 = input("Digite o nome do jogador 1: ")
jogador2 = input("Digite o nome do jogador 2: ")
vitoria1 = (f"O jogador {jogador1} venceu!")
vitoria2 = (f"O jogador {jogador2} venceu!")
print("Pedra... Papel... Tesoouuu-ra!")

jogadap1 = input(f"Digite a jogada do jogador {jogador1}: ").lower()
jogadap2 = input(f"Digite a jogada do jogador {jogador2}: ").lower()

if (jogadap1 != "pedra" and jogadap1 != "papel" and jogadap1 != "tesoura") or (jogadap2 != "pedra" and jogadap2 != "papel" and jogadap2 != "tesoura"):
	print("Erro! Jogada inválida.")

else:
	if jogadap1 == jogadap2:
		print("Temos um empate!")
		
	else:
		if jogadap1 == "pedra":
			if jogadap2 == "papel":
				print(vitoria2)
			else:
				print(vitoria1)

		if jogadap1 == "papel":
			if(jogadap2 == "pedra"):
				print(vitoria1)
			else:
				print(vitoria2)

		if jogadap1 == "tesoura":
			if jogadap2 == "pedra":
				print(vitoria2)
			else:
				print(vitoria1)
