import os
from datetime import datetime

current_date = datetime.now().strftime('%d-%b-%Y')
old_name = r"C:\Excercises\\sales.txt"
new_name = r"C:\Excercises\\sales" + current_date + ".txt"
os.rename(old_name, new_name)
