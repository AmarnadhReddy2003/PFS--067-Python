# Library Management System 
# Project Idea - Students,Faculty, Management,Book issuing and retrieving, updating the ooks etc.
# Basic Book class
#Abstraction 
from abc import ABC,abstractmethod

class LibraryItem(ABC):
    @abstractmethod
    def display(self):
        pass
    @abstractmethod
    def get_type(self):
        pass


class Books(LibraryItem):
    total_books=0
    def __init__(self,book_id,title,author):
        self.book_id=book_id
        self.title=title
        self.author=author
        self.__is_available=True   # (Private Variable)
        Books.total_books +=1

    # Encapsulation use is about we don't want anyone to modify important information
    def issue_book(self):
        if self.__is_available:
            self.__is_available=False
            print('Book issued Sucessfully')
        else:
            print('Book already Issued')

    def return_book(self):
        self.__is_available=True
        print('Book returned Sucessfully')

    def is_available(self):
        return self.__is_available
    
    def display(self):
        print('Book Id: ', self.book_id)
        print('Title: ',self.title)
        print('Author: ',self.author)
        print('Avilable: ',self.is_available())

    def get_type(self):
        return 'Book'

    # Operator Overloading
    def __eq__(self,other):
        if isinstance(other,Books):
            return self.book_id==other.book_id
        return False

    def __str__(self):
        return f"{self.title} by {self.author}"

# EBook
class EBook(Books):
    def __init__(self,book_id,title,author,file_size):
        super().__init__(book_id,title,author)
        self.file_size=file_size

    # Method Overriding
    def issue_book(self):
        print(f"'{self.title}' eBook access granted.")

    def get_type(self):
        return 'EBook'

    def display(self):
        print(
            f"Id: {self.book_id} | "
            f"Title: {self.title} | "
            f"Author: {self.author} | "
            f"File Size: {self.file_size}"
        )

# printed Book 
class PrintedBook(Books):
    def __init__(self,book_id,title,author,pages):
        super().__init__(book_id,title,author)
        self.pages=pages

    def issue_book(self):
        if self.is_available():
            print(f"Printed Book '{self.title}' issued physically.")
            super().issue_book()
        else:
            print('Book already Isuued')

    def get_type(self):
        return 'PrintedBook'

    def display(self):
        super().display()
        print("Pages: ", self.pages)

# Member class
class Member:
    def __init__(self,member_id,name):
        self.member_id=member_id
        self.name=name
        self.borrowed_books=[]

    def borrow_book(self,book):
        if book.is_available():
            book.issue_book()
            self.borrowed_books.append(book)
            print(f"{self.name} barrowed (book.title)")
        else:
            print(f"{book.title} is not avaialble.")

    def return_book(self,book):
        if book in self.borrowed_books:
            book.return_book()
            self.borrowed_books.remove(book)
            print(f"{self.name} returned {book.title}")
        else:
            print('Book was not borrowed by this member.')

    def display_member(self):
        print('\n Member Id: ', self.member_id)
        print('Name: ',self.name)
        print('Borrowed Books: ')
        if not self.borrowed_books:
            print('No books Borrowed')
        else:
            for books in self.borrowed_books:
                print('-', books)


# Student Member
class StudentMember(Member):
    def __init__(self,member_id,name,college):
        super().__init__(member_id,name)
        self.college=college

    def display_member(self):
        super().display_member()
        print('College:', self.college) 

# Faculty Member
class FacultyMember(Member):
    def __init__(self,member_id,name,department):
        super().__init__(member_id,name)
        self.department=department

    def display_member(self):
        super().display_member()
        print('Department: ', self.department)

class Library:
    def __init__(self,name):
        self.name=name
        self.books=[]
        self.members=[]

    # Add book
    def add_book(self,book):
        self.books.append(book)
        print(f"Book {book.title} added sucessfully")

    # Remove Book
    def remove_book(self,book_id):
        for book in self.books:
            if book.book_id==book_id:
                self.books.remove(book)
                print('Book removed sucessfully')
                return
        print('Book not found')

    # Register Member
    def register_member(self,member):
        self.members.append(member)
        print(f'Member {member.name} added sucessfully')

    # Search book logic
    def search_book(self,title=None,author=None):
        found=False
        for book in self.books:
            if (title and title.lower() in book.title.lower()):
                book.display()
                found= True
            elif (author and author.lower() in book.author.lower()):
                book.display()
                found=True
        if not found:
            print('No book found')

    # Display books
    def display_books(self):
        print('\n Library Books: ')
        if not self.books:
            print('No books avaialble')
            return
        for book in self.books:
            book.display()

    # Display Numbers
    def display_members(self):
        print('\n ------ Members------ ')
        for member in self.members:
            member.display_member()

    # Find Member
    def find_member(self,member_id):
        for member in self.members:
            if member.member_id==member_id:
                return member
        return None
    
    # Find Book
    def find_book(self,book_id):
        for book in self.books:
            if book.book_id == book_id:
                return book
        return None        

library=Library('ABC Central Library')
book1= Books(101,'Python','Guido')
book2=PrintedBook('102','Java','Van',500)
book3=EBook(103,'Machin Learning','Andrew','10MB')
library.add_book(book1)
library.add_book(book2)
library.add_book(book3)
student=StudentMember(1,'Ram','ABC College')
faculty=FacultyMember(2,'Dr.Gopi','CSE')
library.register_member(student)
library.register_member(faculty)
library.display_books() 
student.borrow_book(book1)
student.return_book(book1)
library.search_book(title='PyTHon')
library.search_book(author='guido')
library.search_book
