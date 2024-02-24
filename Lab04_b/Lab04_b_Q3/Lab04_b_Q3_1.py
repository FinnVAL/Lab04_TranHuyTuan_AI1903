def count_uppercase(file_name):
    with open(file_name, 'r') as f:
        count = 0
        for line in f:
            for i in line:
                if i.isupper():
                    count += 1
    return count

try:
    n = str(input("Nhập vào tên file:"))
    print(count_uppercase(n))
except:
    print("File không tồn tại")
