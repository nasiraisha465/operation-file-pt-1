file1 = open('codingal.txt','r')
file2 = open('codingalupdated.txt','w')
#reading each line from original
# text file
for line in file1.readlines():
    #reading all lines that do not
    #begin with "codingal"
    if not(line.startswith('Coding')):
        # printing thise lines
        print(line)
        # storing only thoose lines that
        # do not begin with "coding"
        file2.write(line)
# close and save the files
file2.close()
file1.close()
