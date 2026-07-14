class BookStore:

    NoOfBooks = 0

    def __init__(self):
        self.BookName = ""
        self.Author = ""

        BookStore.NoOfBooks += 1

    def Accept(self):
        self.BookName = input("Enter BookName :")
        self.Author = input("Enter Name of Author :")

    def Display(self):
        print(f"{self.BookName} by {self.Author} . No of Books : {BookStore.NoOfBooks}")

bobj1 = BookStore()

bobj1.Accept()
bobj1.Display()

bobj2 = BookStore()

bobj2.Accept()
bobj2.Display()

