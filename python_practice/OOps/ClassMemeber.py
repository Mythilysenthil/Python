class Display:
    def display(self):
        print("Welcome")
    def display_name(self, name):
        print(name)
obj = Display()
obj.display()
name = input("Enter a name: ")
obj.display_name(name)

class Myclass:
    x = 5
    def display(self):
        print("i am inside the function")
obj = Myclass()
print('state: ',obj.x)
print('Behaviour: ')
obj.display()        