class Book:
    def __init__(self,title,author,price):
        super().__init__()
        self.title=title
        self.author=author
        self.price=price

#To DO: the __eq__ method checks the equality between 2 objs
    def __eq__(self,value):

        if not isinstance(value,Book):
            raise ValueError("Cant compare book to non book")
        return(self.title == value.title and 
        self.author == value.author and
        self.price == value.price)
#To DO:  the __ge__ method establishes >= relationship b/n 2 objs
    def __ge__(self,value):

        if not isinstance(value,Book):
            raise ValueError("Cant compare book to non book")
        return(self.price >= value.price)
    #TO DO: the __lt__ method establishes < relationship b/w 2 objs

    def __lt__(self,value):

        if not isinstance(value,Book):
            raise ValueError("Cant compare book to non book")
        return(self.price < value.price)  

b1 = Book("War an peace", "Leo" , 39)
b2 = Book("War", "Leojeo" , 29) 
b3 = Book("War an peace", "Leo" , 39) 
b4 = Book("This is me", "Leonard" , 24)   

#TO DO: Check for equality
print(b1 == b3)
print(b2 >= b1)
print(b2 < b1)

##TO DO: Now we can sort the objs too
##book uses __lt__ function
books = [b1, b3, b4, b2] 
books.sort()
print([book.title for book in books])