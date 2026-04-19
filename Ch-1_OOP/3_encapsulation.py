# Access Modifiers
# public 
# protected
# private
class MyClass: 
    
    def __init__(self, first, second, third):
        self.first = first
        self.second = second
        self.__var1 = "See" #private
        self._third = third #protected
    
    def func1(self):
        print(f"func1 , {self.__var1}")

    def func2(self):
        print(f"func2 , {self._third}")

    #private method
    def __func3(self):
        print("private method")

    def call_private(self):
        self.__func3()

obj1 = MyClass("first", "second","third var")
obj1.func1()
obj1.func2()

# This will not give error but it will create a new variable dyn2 in the object and assign the value "stu" to it.
# It will not change the value of __var1 which is a private variable.
obj1.dyn2 = "stu"
print(obj1.dyn2) 

# don't do this in code as this is protected variable
obj1._third = "change this"

print(obj1._third) 
# It will print "third var" because _third is a protected variable and it can be 
# accessed outside the class but it is not recommended to do so. It is just a convention to 
# use _ before the variable name to indicate that it is a protected variable and it should not be accessed outside the class.

