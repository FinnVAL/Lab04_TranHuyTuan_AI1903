import os

file_path = r"C:\Excercises\\sample.txt"

os.umask(0)
f = open(os.open(file_path, os.O_CREAT | os.O_WRONLY, 0o777), 'w')
