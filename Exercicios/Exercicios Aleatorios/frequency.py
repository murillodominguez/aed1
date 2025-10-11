def order_by_frequency(text_in):
    found = []
    frequencies = []

    for word in text_in:
        if word in found:
            continue
        print(f'Estou no {word}')
        c = 0
        for compare_word in text_in:
            if compare_word in found:
                continue
            print(compare_word)
            if word == compare_word:
                c += 1
                print(c)
        frequencies.append(c)
        found.append(word)
    

    for i, frequency in enumerate(frequencies):
        for j in range(i+1, len(frequencies)):
            comp_frequency = frequencies[j]
            if frequency < comp_frequency:
                temp = frequencies[i]
                frequencies[i] = frequencies[j]
                frequencies[j] = temp
                temp = found[i]
                found[i] = found[j]
                found[j] = temp

    words_ordered_by_frequency = found
        
    return words_ordered_by_frequency

text_in = 'breno breno rafa breno murillo breno murillo rafa murillo murillo'.split()

result = order_by_frequency(text_in)
print(result)