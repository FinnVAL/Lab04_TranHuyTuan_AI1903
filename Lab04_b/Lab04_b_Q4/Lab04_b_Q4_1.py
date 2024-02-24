def hash_display(file_name):
    with open(file_name, 'r') as f:
        text = f.read()
        for i in range(len(text)):
            print(text[i] + '#', end='')

hash_display('matter.txt')
