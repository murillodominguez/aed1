a = float(input("Informe a base do retângulo: "))
b = float(input("Informe a altura do retângulo: "))

if a > 0 and b > 0:
	area = a*b
	perimetro = 2*(a+b)
	print(f"A área do retângulo construído é {area} e seu perímetro é {perimetro}")
	
else:
	print(f"ERRO - ({a}) - ({b});\nHá lados negativos.")
