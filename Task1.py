from sys  import argv
script, file = argv

import MainAssgn

Shivanshu = MainAssgn.User()
Shivanshu.adduser("Shivanshu","9xxxxxxxxx")

f = open(file,'w')

f.write(Shivanshu.username)
f.write("\n")
f.write(Shivanshu.ph)