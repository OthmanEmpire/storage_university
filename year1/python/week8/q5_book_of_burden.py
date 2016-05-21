                ### And what a mighty burden it be. ###



class Author():
    """ King Arthur """

    def __init__(self, first_name, last_name, year_birth, place_birth):
        """ King Arthur """
        self.first_name = first_name
        self.last_name = last_name
        self.year_birth = year_birth
        self.place_birth = place_birth


    def __str__(self):
        """ King Arthur """
        template = ("First name: '{}'\nLast name: '{}'\n"
                    "Year of birth: '{}'\nPlace of birth: '{}'\n")
        return template.format(self.first_name, self.last_name,
                               self.year_birth, self.place_birth)

    def __repr__(self):
        """ King Arthur """
        template = ("Author({},{},{},{})")
        return template.format(self.first_name, self.last_name,
                               self.year_birth, self.place_birth)


    
class Book():
    """ King Arthur """

    def __init__(self, title, year_publication, author):
        """ King Arthur """
        self.title = title
        self.year_publication = year_publication
        self.author = author


    def __str__(self):
        """ King Arthur """
        template = "Title: '{}'\nYear of Publication: '{}'\nAuthor: '{}'"
        return template.format(self.title, self.year_publication, self.author)


    def __repr__(self):
        """ King Arthur """
        template = "Book({},{},{})"
        return template.format(self.title, self.year_publication, self.author)





class Library():
    """ King Arthur """

    def __init__(self, books, authors):
        """ King Arthur """
        self.books = books
        self.authors = authors


    def __repr__(self):
        """ King Arthur """
        template = "Library({}, {})"
        return template.format(self.books, self.authors)


    def printAllBooks(self):
        """ King Arthur """
        for book in self.books:
            print(book, "\n")


    def printAllAuthors(self):
        """ King Arthur """
        for author in self.authors:
            print(author, "\n")        
            

    def getBookByAuthor(self, search_author):
        """ King Arthur """
        books_by_author = []

        for book in self.books:
            if(search_author == book.author):
                books_by_author.append(book)

        return books_by_author


    def getBookByBeforeDate(self, search_date):
        """ King Arthur """
        try:
            search_date = int(search_date)
        except TypeError as e:
            print("Invalid search date entered!")

        books_by_before_date = []

        for book in self.books:
            if(int(search_date) >= int(book.year_publication)):
                books_by_before_date.append(book)

        return books_by_before_date


    def addBook(self, add_book):
        """ King Arthur """
        self.books.append(add_book)


    def removeBook(self, remove_book):
        """ King Arthur """
        for book in self.books:
            if(remove_book == book.title):
                self.books.remove(book)
                print("Removed book:\n{}".format(book))
                return

        print("No books have been removed since no match was found "
              "for keyword: '{}'".format(remove_book))


    def addAuthor(self, new_author):
        """ King Arthur """
        self.authors.append(new_author)


    def storeToFile(self, file_name):
        """ King Arthur """
        try:
            with open(file_name, "w") as file_storage:
                for book in self.books:
                    file_storage.write(str(book) + "\n\n")

        except IOError as err:
            print("Could not store the data!", err)






def main():
    """ King Arthur """


    feed = Book('feed', '1990', 'othman')
    banana = Book('apple', '1995', 'carrot')
    science = Book('Mercury', '1996', 'feed')
    books = [feed, banana, science]

    othman = Author('othman', 'alikhan', '1994', 'Khobar')

    burden = Library(books, [othman])



    print("Welcome to the Library of Burden, where the sweat of the brow "
          "is engraved into history itself!\n\n")
    print("1. View all the books in the library--the total burden\n"
          "2. View all the authors--the wielders of burden\n"
          "3. View all the books before a specified date--the past burden\n"
          "4. View all the books by an author--the burden of man\n"
          "5. Add a new book to the library--increasing it's burden\n"
          "6. Add a new author--spreading the burden\n"
          "7. Store the library onto a record--the burden is not so easily "
          "erased...\n")
    choice = input("Please select your division: ")


    if(choice == '1'):
        burden.printAllBooks()


    elif(choice == '2'):
        burden.printAllAuthors()


    elif(choice == '3'):
        year = input("Of what year would you like to view the sins of? ")
        books_found = burden.getBookByBeforeDate(year)

        if(books_found):
            for book in books_found:
                print(book)
        else:
            print("No self recorded sins at the very least.")


    elif(choice == '4'):
        author = input("Which sinner's book would you like to examine? ")
        books_found = burden.getBookByAuthor(author)

        if(books_found):
            for book in books_found:
                print(book)
        else:
            print("Such a sinner does not exist--a mere figment of your "
                  "limited imagination.")


    elif(choice == '5'):
        print("Put forth your written burden\n\n")
        title = input("Title: ")
        year_of_publication = input("Year of Publication: ")
        author = input("Author: ")

        new_book = Book(title, year_of_publication, author)
        burden.addBook(new_book)

    elif(choice == '6'):
        print("Thou sinner may enter to repent\n\n")
        first_name = input("First name: ")
        last_name = input("Last name: ")
        year_birth = input("Year birth: ")
        place_birth = input("Place birth: ")

        new_author = Author(first_name, last_name, year_birth, place_birth)
        burden.addAuthor(new_author)


    elif(choice == '7'):
        print("The burden will not so easily fade away\n\n")
        file_store = input("Name of file to store: ")
        burden.storeToFile(file_store)



main()