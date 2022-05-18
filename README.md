# Car-Rental-Management

#question


Main classes:

class manufacturers(object):
   # def __init__(self,name,country):
    #    self.name = name
     #   self.country = country
    def addman(self,mname,country):
        self.mname=mname
        self.country = country
class Car():
    #def __init__(self, name, country,model):
     #   super().__init__(name, country)    
      #  self.model = model
    #super().mname
    def addcar(self,model,name):
        self.model = model
        self.carmanname =name

class User():
    #def __init__(self, name, country, model):
        #super().__init__(name, country, model)
        #self.username = username
        #self.ph = ph
    def adduser(self,username,ph):
        self.username = username
        self.ph = ph
        
#Task1
from sys  import argv
script, file = argv

import MainAssgn

Shivanshu = MainAssgn.User()
Shivanshu.adduser("Shivanshu","861857")

f = open(file,'w')

f.write(Shivanshu.username)
f.write("\n")
f.write(Shivanshu.ph)

#task2
from sys  import argv
script, file = argv

#import Task1

f = open(file,'r')

print("USERNAME:",f.readline())
print("\nUSER CONTACT NUMBER:",f.readline())

f.close()

#Task3
import MainAssgn

Man = MainAssgn.manufacturers()

Man.addman("BMW","GERMANY")

#Task4
import Task3

print("MANUFACTURERS NAME:",Task3.Man.mname)
print("MANUFACTURER COUNTRY:",Task3.Man.country)

#Task5

import MainAssgn

Car1 = MainAssgn.Car()
Car1.addcar("BX121","GERMANY")

print(Car1.model)
print(Car1.carmanname)
        
