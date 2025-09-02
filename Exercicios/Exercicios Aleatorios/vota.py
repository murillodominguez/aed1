from datetime import date

birth_date = input("Digite sua data de nascimento (DD/MM/AAAA): ")
ano = int(birth_date[6:10])
mes = int(birth_date[3:5])
dia = int(birth_date[0:2])
ano_atual = date.today().year
mes_atual = date.today().month
dia_atual = date.today().day
idade = ano_atual - ano

if mes_atual < mes or mes_atual == mes and dia_atual < dia:
	idade -= 1

if idade < 16:
	print("Não pode votar")
else:
	if idade < 18 or idade >= 70:
		print("Voto facultativo")
	else:
		print("Voto obrigatório")
