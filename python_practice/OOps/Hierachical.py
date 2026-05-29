class num:
    def __init__(self):
        self.x = 20
        self.y = 10

class add(num): # add inherit from num
    def findsum(self):
        self.z = self.x + self.y
        print("Sum is: ",self.z)

class sub(num):
     def findsub(self): # similar sub also inherit from num
        self.z = self.x - self.y
        print("Sub is: ",self.z)        

obj1 = add()
obj1.findsum()

obj2 = sub()
obj2.findsub()