class Student:
    def __init__(self, name, age):
        self.name = name
        self.__age = age #private
    def getAge(self):
        return self.__age  #private is accessed by get
    def setAge(self, age):
        self.__age = age
stud = Student("Mary",14)
print("Name: ",stud.name,",Age: ",stud.getAge())  #retriving the age using getter method
stud.setAge(16)
print("Name: ",stud.name,",Age: ",stud.getAge())  #retriving the age using getter method      