from datetime import datetime

current_date = datetime.now().strftime("%d-%m-%Y")
current_datetime = datetime.now().strftime("%d-%m-%Y-%H-%M-%S")

str_current_date = str(current_date)
str_current_datetime = str(current_datetime)

file_name_1 = str_current_date+".txt"
file_1 = open(file_name_1, 'w')

print("created", file_1.name)
file_1.close()

file_name_2 = str_current_datetime+".txt"
file_2 = open(file_name_2, 'w')

print("created", file_2.name)
file_2.close()

file_name_3 = r"C:\Excercises\\" + current_datetime +".txt"
with open(file_name_3, 'w') as fp:
    print("created", file_name_3)