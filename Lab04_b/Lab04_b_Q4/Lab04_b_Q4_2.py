def JTOI(file_name):
    with open(file_name, 'r') as file:
        content = file.read()
    corrected_content = content.replace('J', 'I')
    print(corrected_content)

JTOI('WORDS.TXT')