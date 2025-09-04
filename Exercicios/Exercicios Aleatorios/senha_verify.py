# - Crie uma função que "quebre" uma senha

# Para facilitar, considere testes com letra maiúscula

# numeros: 48 - 57
def quebra_senha(senha, minusculas = False, maiusculas = False):
    lensenha = len(senha)
    senha_testada = ''
    while senha_testada != senha:
        k = 48
        while k <= 57:            
            char = chr(k)
            i = 0
            for l in range(48, 58):
                char = chr(l)
                senha_testada += char
                if senha_testada == senha:
                    return senha
                while i < lensenha:
                    senha_testada += char*i
                    
                    if len(senha_testada) == len(senha):
                        break
                    i += 1
            print(senha_testada)
            senha_testada = ''
            k += 1
            


senha = '111'

print(quebra_senha(senha))

# 0000
# 0011
# 11111
# recursividade
#i, j, l