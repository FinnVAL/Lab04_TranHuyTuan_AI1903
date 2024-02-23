import os

list_file = ["sales_1.txt"]
folder = r'C:\Excercises\\'

for f in os.listdir(folder):
    if f in list_file:
        old_name = os.path.join(folder,f)
        name = os.path.splitext(f)[0]
        new_name = os.path.join(folder,name + "_new" +".txt")
        os.rename(old_name,new_name)

print(os.listdir(folder))