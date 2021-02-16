#callable function is used to call object like a function.
#To call a object as if it were a function
#b1=Book("","","")
#b1("","","")
#Generally used if you have objects whose attributes change is required frequently

class Book:
    def __init__(self,title,author,price):
        super().__init__()
        self.title=title
        self.author=author
        self.price=price

    def __str__(self):
        return f"{self.title} by {self.author},costs {self.price}"    

    def __repr__(self):
        return f"title={self.title},author={self.author},price={self.price}"


    def __call__(self,title,author,price):
        self.title=title
        self.author=author
        self.price=price
b1 = Book("tempations","vivesisi","80.0")
b2 = Book("SAMCAT","NPS","60")
b1("SAM the Fat Cat","DPS","90")
print(str(b1))
print(repr(b2))
print(repr(b1))

