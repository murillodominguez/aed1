def compact_to_mvc(filepath, compacted_filepath):
    word_dict = {}
    listed_words = []
    compacted_txt = ""
    with open(filepath, encoding="latin-1") as file:
        content = file.read().split()
    c = 0
    for word in content:
        if word not in listed_words:
            word_dict[word] = str(c)
            c += 1
        compacted_txt += word_dict.get(word) + '|'
        listed_words += [word]
    
    for i, key in enumerate(word_dict):
        if i < len(word_dict) - 1:
            compacted_txt += key + "|"
        else:
            compacted_txt += key

    with open(compacted_filepath, 'w', encoding='latin-1') as file:
        file.write(compacted_txt)

compact_to_mvc('example.txt', 'compact.mvc')

def extract_from_mvc(filepath):
    encoding_dict = {}
    extracted_content = ""

    with open(filepath, encoding="latin-1") as file:
        content = file.read()
    separated_compaction = content.split('|')
    c = 0
    for string in separated_compaction:
        if string[0].isalpha():
            encoding_dict[str(c)] = string
            c += 1

    print(encoding_dict)
    for i, string in enumerate(separated_compaction):
        if string[0].isalpha():
            break
        if i < len(separated_compaction) - 1:
            extracted_content += encoding_dict[string] + " "
        else:
            extracted_content += encoding_dict[string]
    
    with open('extracted.txt', 'w', encoding='latin-1') as file:
        file.write(extracted_content)

extract_from_mvc('compact.mvc')

