import os

try:
    with open('test.txt', 'r') as f:
        f.read()
    os.rename("test.txt","new name.txt")
except:
    print("File does not exit!")