def count_words(file_name):
    with open(file_name, 'r') as f:
        t = f.read()
    words = t.split()
    count = 0
    for word in words:
        if word == 'this' or word == 'these':
            count += 1
    return count

print(count_words('article.txt'))