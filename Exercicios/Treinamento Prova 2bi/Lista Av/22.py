def my_replace(string, antiga, nova, contagem = 1):
    result = ''
    
    i = 0
    j = 0
    temp = []
    while i < len(string):
        if string[i] == antiga[j] and contagem > 0:
            j += 1
            temp += string[i]
        else:
            j = 0
            if len(temp) > 0:
                result += ''.join(temp)
            result += string[i]
            temp = []

        if j == len(antiga):
            j = 0
            result += nova
            contagem -= 1
            temp = []
        i += 1
    contagem -= 1
    return result

result = my_replace('Eu gosto de pizza e piroca', 'pizza', 'relógio', 1)
print(result)