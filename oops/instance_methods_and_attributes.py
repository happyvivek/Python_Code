
#Not allowing overriding the class attribute from some other class.(__attribute)
#Creating private attribute to class so that it can be accesed only inside the class(_attribute)
##hasattr to check if attribute exist in the class obj instantiated.

class Book:
    def __init__(self, title, author, pages, price):
        #TO Do add instance attributes
        self.title = title
        self.author = author
        self.pages = pages
        self.price = price
        self.__secret="This is the secret value"
        #To DO create instance method
    def getprice(self):
        if hasattr(self, "_discount"):
            return self.price - (self.price * self._discount)
        else:
            return self.price



#To DO to give other devlopers a hint that amount attribute is private to this class and cant be accessed outside this class
#Can be used within the logic of the class only so _ defines this
    def setdiscount(self, amount):
        self._discount = amount    


#To DO:  create book instance
b1 = Book("turtle", "Ruskin Bond", 340, 500)
print(b1.getprice())
#We are not limited to create instance attribute inside init function infact we can create it anywhere


#setting the discount

b1.setdiscount(0.25)
print(b1.getprice())
#print(b1.__secret)

#you declare attrribute with __ ,this attribute remains hidden and cannot be seen outside the class
# print(b1.__secret)
#AttributeError: 'Book' object has no attribute '__secret'
#Name Dangling other classes can access but adding _clasname to it
#Eg: _Book__secret so this way attribute overriding is prevented in some other class.

print(b1._Book__secret)






