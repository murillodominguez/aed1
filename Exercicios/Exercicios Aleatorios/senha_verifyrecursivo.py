def quebra_senha(senha, temnumero = True, temletra = False):
    lensenha = len(senha)
    senha_teste = cria_senha('', lensenha)
    if senha_teste == senha:
        return senha_teste
def cria_senha(w, lensenha):
    if len(w) == lensenha:
        return w
    while len(cria_senha(w, lensenha)) < lensenha:
        i = 48
        while i <= 57:
            char = chr(i)
            cria_senha(w+char, lensenha)
            i += 1
quebra_senha('123')