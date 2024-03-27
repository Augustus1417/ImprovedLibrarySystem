from random import randint
from json import load, dump

class Book:
    def __init__(self,title,author,ISBN,available_copies):
        self.title = title
        self.author = author
        self.ISBN = ISBN
        self.available_copies = available_copies

class Patron:
    def __init__(self,name, library_card_number,books_borrowed):
        self.name = name
        self.library_card_number = library_card_number
        self.books_borrowed = books_borrowed

class Library:
    def __init__(self,name):
        self.name = name
        patronDict = open("patrons.json")
        self.patrons = load(patronDict)
        bookDict = open("books.json")
        self.books = load(bookDict)

    def new_book(self,title,author,ISBN,available_copies):
        self.books[ISBN] = (author,title,available_copies)
        print(f"\n\t{title} by {author} has been registered. \n\tISBN: {ISBN} \n\tAvailable Copies: {available_copies}\n")
        with open ("books.json",'w') as f: dump(self.books,f)

    def remove_book(self,ISBN):
        if ISBN in self.books:
            print(f"\n\t{self.books[ISBN][1]} by {self.books[ISBN][0]} has been removed from the library.\n")
            del self.books[ISBN]
            with open ("books.json",'w') as f: dump(self.books,f)
        else: print("\n\tBook not found\n")

    def register_patron(self,name, library_card_number,books_borrowed):
        self.patrons[library_card_number] = (name,books_borrowed)
        print(f"\n\tPatron has been registered. Welcome {name}!\n\tYour Library Card Number is {library_card_number}\n")
        with open ("patrons.json",'w') as f: dump(self.patrons,f)

    def remove_patron(self,library_card_number):
        if library_card_number in self.patrons:
            print(f"\n\t{self.patrons[library_card_number][0]} has been removed from the library records.\n")
            del self.patrons[library_card_number]
            with open ("patrons.json",'w') as f: dump(self.patrons,f)
        else: print("\n\tPatron not found\n")

    def borrow_book(self,library_card_number,ISBN,amount):
        if library_card_number in self.patrons:
            if ISBN in self.books:
                if amount <= self.books[ISBN][2]:
                    self.books[ISBN][2] -= amount
                    self.patrons[library_card_number][1] += amount
                    with open ("patrons.json",'w') as f: dump(self.patrons,f)
                    with open ("books.json",'w') as g: dump(self.books,g)
                    if amount > 1:print(f"\n\t{self.patrons[library_card_number][0]} has borrowed {amount} copies of {self.books[ISBN][1]}.\n")
                    if amount == 1:print(f"\n\t{self.patrons[library_card_number][0]} has borrowed {amount} copy of {self.books[ISBN][1]}.\n")
                else: print("\n\tInvalid amount.\n")
                if amount == 0: print("\n\tInvalid amount\n")
            else: print("\n\tBook not found\n")
        else: print("\n\tPatron not found\n")
               
    def return_book(self,library_card_number,ISBN,amount):
        if library_card_number in self.patrons:
            if ISBN in self.books:
                if amount <= self.patrons[library_card_number][1]:
                    self.books[ISBN][2] += amount
                    self.patrons[library_card_number][1] -= amount
                    with open ("patrons.json",'w') as f: dump(self.patrons,f)
                    with open ("books.json",'w') as g: dump(self.books,g)
                    if amount > 1:print(f"\n\t{self.patrons[library_card_number][0]} has returned {amount} copies of {self.books[ISBN][1]}.\n")
                    if amount == 1:print(f"\n\t{self.patrons[library_card_number][0]} has returned {amount} copy of {self.books[ISBN][1]}.\n")
                else: print("\n\tInvalid amount\n")
                if amount == 0: print("\n\tInvalid amount\n")
            else: print("\n\tPatron not found\n")
        else: print("\n\tPatron not found\n")

    def display_books(self):
        print("\n\t\tAvailable Books:")
        for book in self.books: print(f"\n\t{self.books[book][1]} by {self.books[book][0]} \n\t\tISBN: {book} \n\t\tAvailable Copies: {self.books[book][2]}")

    def display_patrons(self):
        print("\n\t\tRegistered Patrons:")
        for patron in self.patrons: print(f"\n\t\tName: {self.patrons[patron][0]}\n\t\tLibrary Card Number: {patron} \n\t\tBooks Borrowed: {self.patrons[patron][1]}")

    def clearbooks(self):
        self.books.clear()
        with open ("books.json",'w') as g: dump(self.books,g)
        print("Book records have been cleared.")
    
    def clearpatrons(self):
        self.patrons.clear()
        with open ("patrons.json","w") as f: dump(self.patrons,f)
        print("Patron records have been cleared.")
   
def line():
    for x in range(60):print("-",end="")
    print()

def main():
    library = Library("Library")
    while True:
        line()
        print("1. Add new book"
              "\n2. Remove book"
              "\n3. Register new patron"
              "\n4. Remove patron"
              "\n5. Borrow book"
              "\n6. Return book"
              "\n7. Display available books"
              "\n8. Display patrons registered"
              "\n9. Exit")
        line()
        choice = input("Enter choice 1/2/3/4/5/6/7/8/9: ")
        line()
        try:
            if choice == "1":
                    title = input("Enter book title: ")
                    author = input("Enter book author: ")
                    ISBN = str(randint(1000000000,9999999999))
                    available_copies = int(input("Enter available copies: "))
                    line()
                    library.new_book(title,author,ISBN,available_copies)
                    continue
            if choice == "2":
                ISBN = input("Enter ISBN: ")
                line()
                library.remove_book(ISBN)
                continue
            if choice == "3":
                name = input("Enter your name: ")
                library_card_number = str(randint(10000,99999))
                line()
                library.register_patron(name,library_card_number,0)
                continue
            if choice == "4":
                library_card_number = input("Enter library card number: ")
                line()
                library.remove_patron(library_card_number)
                continue
            if choice == "5":
                library_card_number = input("Enter library card number: ")
                ISBN = input("Enter ISBN: ")
                amount = int(input("Enter the amount of copies to borrow: "))
                line()
                library.borrow_book(library_card_number,ISBN,amount)
                continue
            if choice == "6":
                library_card_number = input("Enter library card number: ")
                ISBN = input("Enter ISBN: ")
                amount = int(input("Enter the amount of copies to return: "))
                line()
                library.return_book(library_card_number,ISBN,amount)
                continue
            if choice == "7":
                library.display_books()
                continue
            if choice == "8": 
                library.display_patrons()
                continue
            if choice == "9":
                print("Program will now close. Goodbye!")
                break
            if choice == "CLEARBOOKS": 
                library.clearbooks()
                continue
            if choice == "CLEARPATRONS": 
                library.clearpatrons()
                continue
            else: print("\n\tError, try again.\n")
        except: 
            line() 
            print("\n\tError, input must be a number. Try again.\n")
    quit()
    
if __name__ == "__main__": main()