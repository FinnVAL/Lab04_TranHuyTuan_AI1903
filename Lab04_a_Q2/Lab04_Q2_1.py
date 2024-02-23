file_name = "newfile.txt"
f = open(file_name,'w')
f.write("content")
print("Done Writing")
print("This is new content")
f.close()
