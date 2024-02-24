def read_lines(file_name):
    with open(file_name, 'r') as f:
        for line in f:
            print(line, end='')

read_lines('poem.txt')
