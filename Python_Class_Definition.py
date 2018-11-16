# Class definition
class Student:
  def __init__(self, first, last):
    self.first = first
    self.last = last

  def sayName(self):
    print self.last, self.first

# Your code executes here 
#
#
# Instantiate student called "f"
f=Student("Jack","Mack")
print f.first
