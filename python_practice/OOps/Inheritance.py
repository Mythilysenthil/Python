class Student:
    def getStudentInfo(self):
        self.__rollno = input("Enter the rollNo: ")
        self.__name = input("Enter the name: ")
    def printStudentInfo(self):
        print("Roll No:", self.__rollno)
        print("Name:", self.__name)

class Marks(Student):
    def getmarks(self):
        self.getStudentInfo()
        self.__marks1 = float(input("Enter marks for sub 1: "))
        self.__marks2 = float(input("Enter marks for sub 2: "))
        self.__marks3 = float(input("Enter marks for sub 3: "))
    def printmarks(self):
        self.printStudentInfo() 
        print("Marks1: ",self.__marks1)
        print("Marks2: ",self.__marks2)
        print("Marks3: ",self.__marks3)
    def totalCal(self):
        return self.__marks1 + self.__marks2 + self.__marks3  
       
class Results(Marks):
    def getResult(self):
        self.getmarks()
        self.__total = self.totalCal()
    def pullResult(self):
        self.printmarks()
        print("Total marks out of 300: ",self.__total)

obj = Results()
obj.getResult()
obj.pullResult()
