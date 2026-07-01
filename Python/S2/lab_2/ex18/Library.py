class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.availability = True

    def get_availability(self):
        if self.availability == True:
            return "available"
        else:
            return "not available"
        
    def __str__(self):
        return f"{self.title} by {self.author} -- {self.get_availability()}"
    
class Library:
    def __init__(self):
        self.books = []

    def add_book(self):
        name = input("Input the name of the book: ")
        author = input("input the name of the author: ")
        book = Book(name, author)
        self.books.append(book)

    def search(self):
        search = input("Title of your book")
        for i in self.books:
            if i.title == search:
                return f"Found: {i.title} from {i.author} -- {i.get_availability()}"
        
        return "title not found!"
    
    def borrow(self):
        search = input("Title of your book")
        for i in self.books:
            if i.title == search:
                if i.get_availability == False:
                    print(f"{i.title} is currently not available!")
                    return   
                else:    
                    print(f"You have lend out {i.title}")
                    i.availability = False
                    return

    def return_book(self):
        search = input("Title of your book")
        for i in self.books:
            if i.title == search:
                print(f"You have returned {i.title}")
                i.availability = True

    def catalogue(self):
        print("--- current catalogue ---")
        for i in self.books:
            print(i)