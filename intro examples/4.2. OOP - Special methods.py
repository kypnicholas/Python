
## SPECIAL METHODS (or MAGIC/DUNDER MEHTODS) ## 
# Allow us to use Python specific functions on objects created through our class.
# Defined using double underscores. 
# __init__(), __str__(), __len__(), __del__()

class Book:
    def __init__(self, title, author, pages):
        print("A book is created")
        self.title = title
        self.author = author
        self.pages = pages

    def __str__(self):
       return "Title: %s, author: %s, pages: %s" %(self.title, self.author, self.pages)

    def __len__(self):
        return self.pages

    def __del__(self):
        print("A book is destroyed")

# TEST
book = Book("Python Rocks!", "Jose Portilla", 159)

# Special Methods
print(book)
print(len(book))
del book