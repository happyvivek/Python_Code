
#Class Definition
#() is required only when you want to indicate that class inherits from another class
#override the __init__ function
#init function(initializer function) is a special function to initialize thenew obj with info
#init function is syninymous to constructor in java but obj is already created/initialized when
#  __init is called
#init function is the first function to call before any other function to callin class

#what is self??
#whenever we intantiate a function on python obj,1 aregument by default passes is the obj name.

class book:
    def __init__(self,title):
        self.title=title

#Create Instance of the class

##b1 prints the addr or ref to the b1 obj
b1 = book("This is the title of this book")
b2 = book("This is 2nd instantiation of book class")

#Print the class and property
##b1 prints the addr or ref to the b1 obj
print (b1)
print (b1.title)
