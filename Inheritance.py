#Inheritance

#parent class one
class Parent:
    def assign_string_one(self,str1):
        self.str1= str1
    def show_string_one(self):
        return self.str1

class Derived(Parent):
    def assign_string_two(self,str2):
        self.str2= str2
    def show_string_two(self):
         return self.str2

#object create
d1= Derived()
d1.assign_string_one("one")
d1.assign_string_two("two")
#invoking methods

print(d1.show_string_one())
print(d1.show_string_two())


