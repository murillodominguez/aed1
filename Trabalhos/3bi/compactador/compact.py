import sys

def compact_to_mvc(filepath, compacted_filepath):
    word_dict = {}
    listed_words = []
    compacted_filepath = compacted_filepath + ".mvc"
    compacted_txt = ""
    try:
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

    except FileNotFoundError:
        print(f"Couldn't find the file to compact '{sys.argv[1]}'")

    with open(compacted_filepath, 'w', encoding='latin-1') as file:
        file.write(compacted_txt)

if __name__ == "__main__":
    try:
        compact_to_mvc(sys.argv[1], sys.argv[2])
    except IndexError:
        print("ERR! python compact.py missing options. OPTIONS: [filename] [extracted filename]")
    