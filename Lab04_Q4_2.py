import os

folder = r'C:\Excercises\\'
num = 1

for f in os.listdir(folder):
    old_name = folder + f
    new_name = folder + "sales_" + str(num) +".txt"
    os.rename(old_name,new_name)
    num += 1

print("All Files Renamed")
print("New Names are")
print(os.listdir(folder))