#self is not a keyword, just a convention
class MyClass: 
    #class variables
    var1  = "Chetan"
    var2  = "Upreti"
    def __init__(self, first, second):
        #instance variables
        self.first = first
        self.second = second

    def func1(self):
        print(f"func1 , {self.first}")

    def func2(self):
        print(f"func2 , {self.second}")

obj1 = MyClass("first", "second")
obj1.func1()
obj1.func2()

# Another Way to call the function
# MyClass.func1(obj1)

newObj = MyClass("first", "second")
newObj.var1 = "Mukesh"

print(newObj.var1)