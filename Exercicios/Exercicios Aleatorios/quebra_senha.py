# - Crie uma função que "quebre" uma senha

# Para facilitar, considere testes com letra maiúscula

def quebra_senha(senha):
    indexes = []
    allowed = '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    base = len(allowed)
    tamanho = len(senha)

    i = 0
    while i < tamanho:
        indexes += [0]
        i += 1

    guess = ''
    while guess != senha:
        guess = ''
        for idx in indexes:
            guess += allowed[idx]
        print(guess)
        if guess == senha:
            return f'A senha é {guess}'
        pos = tamanho - 1
        while pos >= 0:
            indexes[pos] += 1
            if indexes[pos] < base:
                break
            indexes[pos] = 0
            pos -= 1
            

quebra_senha('12aZ')