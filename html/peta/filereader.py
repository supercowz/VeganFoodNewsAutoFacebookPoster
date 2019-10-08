f= open("county_adjacency.txt","r")
f2= open("data.json", "w")

lines = f.readlines()
count = 0
f2.write("[")

iscomma = False
for line in lines:
    if (line.startswith("\t\t")):
        if (iscomma):
            f2.write(",")
        else:
            iscomma = True
            
        f2.write(line.replace("\t\t", "").replace("\n", ""))
    else:
        f2.write("]},")
        f2.write("{\"name\":" + line.replace("\n", "") + ", \"nearby\":[")
        iscomma = False
    
f2.write("]")

f.close()
f2.close()
