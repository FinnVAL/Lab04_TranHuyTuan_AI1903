def count_words(file_name):
    with open(file_name, 'r') as f:
        t = f.read()
    words = t.split()
    num_words = len(words)
    print('Total words are',num_words)

try:
    n = str(input("Nhập vào tên file:"))
    count_words(n)
except:
    print("File không tồn tại")
