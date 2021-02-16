#__str__  is used to provide user friendly string description to user.
#Genrally displayed to end user

#__repr__ string is more developer firendly,ideally can be used to creat obj in current state.
#Commonly used for debugging purpose.

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
b1 = Book("tempations","vivesisi","80.0")
b2 = Book("SAMCAT","NPS","60")

print(str(b1))
print(repr(b2))

