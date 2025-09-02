senha = "AED1_2025"
senha_palpite = None
tent = 10
while senha_palpite != senha and tent > 0:
    senha_palpite = input("Digite a senha: ")
    tent -= 1
if senha_palpite == senha:
    print("Sistema acessado!")
else:
    print("Acesso negado")
    