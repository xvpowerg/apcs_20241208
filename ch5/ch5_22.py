fileName = "Poem.txt"
fin = open(fileName)
line = fin.readline()
while line:
    print(line,end="")
    line = fin.readline()

