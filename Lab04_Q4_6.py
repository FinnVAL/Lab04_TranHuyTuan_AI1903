import glob
import os

old_folder = r"C:\Excercises\\"
new_folder = r"C:\Excercises\new_demo\\"

old_name = old_folder + "expense.txt"
new_name = new_folder + "expense.txt"

os.rename(old_name, new_name)