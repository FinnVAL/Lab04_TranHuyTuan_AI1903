import os

folder = r"C:\Excercises\\"

print('Before rename')
f = os.listdir(folder)
print(f)

for i in f:
    old_name = os.path.join(folder, i)

    new_name = old_name.replace('.txt', '.pdf')
    os.rename(old_name, new_name)

print('After rename')
print(os.listdir(folder))
