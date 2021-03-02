
from dataclasses import dataclass
@dataclass

class Book:
    title: str
    author: str
    pages: str
    price: float

    def book_info(self):
        return f"{self.author}"


b1 = Book("SAM", "NPS", "100", "100.5")
b2 = Book("SAM1", "Geocide", "101", "102")
b3 = Book("SAM", "NPS", "100", "100.5")

#Dataclass implementation of __repr__

print(b1)
#Dataclass implementation of __eq__
print(b1 == b3)

print(b1.title)
print(b2.title)