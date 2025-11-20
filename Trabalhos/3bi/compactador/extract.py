import sys

print(sys.argv)

def extract_from_mvc(filepath, extracted_path):
    encoding_dict = {}
    extracted_content = ""
    try:
        with open(filepath, encoding="latin-1") as file:
            content = file.read()
        separated_compaction = content.split('|')
        c = 0
        for string in separated_compaction:
            if string[0].isalpha() or string == '\n':
                encoding_dict[str(c)] = string
                c += 1

        for i, string in enumerate(separated_compaction):
            if string[0].isalpha():
                break
            if i < len(separated_compaction) - 1 and encoding_dict[string] != '\n':
                extracted_content += encoding_dict[string] + " "
            else:
                extracted_content += encoding_dict[string]
    
    except FileNotFoundError:
        print(f"Couldn't find the file to compact '{sys.argv[1]}'")
    
    with open(extracted_path, 'w', encoding='latin-1') as file:
        file.write(extracted_content)

if __name__ == "__main__":
    try:
        extract_from_mvc(sys.argv[1], sys.argv[2])
    except IndexError:
        print("ERR! python compact.py missing options. OPTIONS: [filename] [extracted filename]")
    