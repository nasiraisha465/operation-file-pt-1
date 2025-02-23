# open file and read itss contents
file = open('codingal.txt','r')
print(file.read())
file.close()
# open file and read its beginning 8 charters
file = open('codingal.txt','r')
print("\n read in parts \n")
print(file.read(120))
file.close()
#append your name and age in the file
file = open('codingal.txt','a')
file.write("Hi! I am Penguin and I am 1 yr old.")
file.close()