def replace_char_with_ascii_pace(txt, key):
    replaced_str = ''
    for letter in txt:
        charcode = ord(letter)
        if charcode > 127:
            charcode = charcode % 127
        replaced_str += chr(charcode + key)
    return replaced_str

def decode_replaced_char_with_ascii_pace(txt, key):
    normalized_str = ''
    for letter in txt:
        charcode = ord(letter)
        if charcode > 127:
            charcode = charcode % 127
        normalized_str += chr(charcode - key)
    return normalized_str

teste = replace_char_with_ascii_pace('eu sei programar!', 5)
decoded_test = decode_replaced_char_with_ascii_pace(teste, 5)

def brute_force_test_char_with_ascii_pace(txt):
    for i in range(127*2):
        i = -i
        print(decode_replaced_char_with_ascii_pace(txt, i))
print(teste)
print(decoded_test)

brute_force_test_char_with_ascii_pace('Lqug')