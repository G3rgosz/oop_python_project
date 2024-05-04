class Book:

    LOCATION = "Én könyvtáram"
    def __init__(self, title, price): #konstruktor
        # print("lérejöttem")
        self.title = title
        self.price = price

#    def writeToConsole(self):
#        print(f"A könyv címe {self.title} és az ára {self.price}")
    def __str__(self):
        return f"A könyv címe {self.title} és az ára {self.price}"

    def priceUpdate(self, price):
        self.price = price

class Tag:
    pass

# print(type(my_book))

print(Book.LOCATION)

my_book = Book("Háború és béke", 600)
print(my_book.title, my_book.price)

my_book.priceUpdate(200)
#my_book.writeToConsole()
print(my_book)

other_book = Book("Vaják", 1000)
print(other_book.title, other_book.price)
