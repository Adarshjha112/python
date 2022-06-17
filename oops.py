#classes and project

#class MyClass:
 # x = 5
#p1 = MyClass()
#print(p1.x)


class Phone:

    def set_color(self,color):

       self.color = color
    def show_color(self):
        return self.color

    #object create
P2 = Phone()
P2.set_color("blue") #invoke
P2.show_color()

print(P2.show_color())

#constructor
class ram:
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def employee_details(self):
        print("name",self.name)
        print("age",self.age)
#create object
e1 = ram("r",23)

e1.employee_details()


