#Ý 1 câu Q3:

with open('test.txt', 'w') as f:
    f.seek(0,0)
    f.write("My First Line\nMy Second Line")
    f.close()

#Ý 2 câu Q3:
    
with open('test.txt', 'a') as f:
    f.seek(0,2)
    f.write("\nThis content is added to the end of the file")
    f.close()

#Ý 3 câu Q3:

print("Ý 3 câu Q3:")

with open('test.txt', 'rb') as f:
    f.seek(3,0)
    print(str(f.read(5),'utf-7'))
    f.seek(10,1)
    print(str(f.read(6),'utf-7'))
    f.close()

#Ý 4 câu Q3:
    
print("\nÝ 4 câu Q3:")
    
with open('test.txt', 'rb') as f:
    print(str(f.read(8),'utf-7'))
    f.seek(-5,1)
    print(str(f.read(10),'utf-7'))
    f.close()

#Ý 5 câu Q3:
    
print("\nÝ 5 câu Q3:")

with open('test.txt', 'r') as f:
    f.seek(75)
    print("file handle at:",f.tell())
    f.seek(95)
    print("file handle at:",f.tell())
    f.seek(0)
    print("file handle at:",f.tell())
    print("***Printing File Content***")
    print(f.read())
    print("Demonstrating tell")
    print("***Done***")
    f.seek(95)
    print("file handle at:",f.tell())
    f.close()
