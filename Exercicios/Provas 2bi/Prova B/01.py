def conta_leds(n):
    conta_leds = 0
    for num in n:
        if num == '0':
            conta_leds += 6
        if num == '1':
            conta_leds += 2
        if num == '2':
            conta_leds += 5
        if num == '3':
            conta_leds += 5
        if num == '4':
            conta_leds += 4
        if num == '5':
            conta_leds += 5
        if num == '6':
            conta_leds += 6
        if num == '7':
            conta_leds += 3
        if num == '8':
            conta_leds += 7
        if num == '9':
            conta_leds += 6
    return f'{conta_leds} leds'

result = conta_leds('2819311')

print(result)