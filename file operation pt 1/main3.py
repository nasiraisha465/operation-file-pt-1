fn = open('codingal.txt','r')
# open other fuile in write mode
fni = open('codingalupdated.txt','w')
# read the content of the file line by line 
cont = fn.readlines()
type(cont)
for i in range(1, len(cont)+1):
    if(i % 2 != 0):
        fni.write(cont[i-1])
    else:
        pass
    # close the file
fni.close()
# open file read mode
fni = open('codingalupdated.txt','r')
# read the content of the file
cont1 = fni.read()
# print the content of the file
print(cont1)
# close all files
fn.close()
fni.close()