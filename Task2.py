from sys  import argv
script, file = argv

#import Task1

f = open(file,'r')

print("USERNAME:",f.readline())
print("\nUSER CONTACT NUMBER:",f.readline())

f.close()
