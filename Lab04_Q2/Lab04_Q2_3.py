lines =["Name: Emma", "Address: 221 Baker Street", "City: London"]
with open("newfile.txt",'w') as f:
    for line in lines:
        f.write("%s\n" % line)
