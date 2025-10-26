class Book:
    #A class to represent a book with title, author, and publication year.

    def __init__(self, title, author, year):
        #Initialize a Book instance with title, author, and publication year.
        self.title = title
        self.author = author
        self.year = year

    def __str__(self):
        #Return a user-friendly string representation of the book.
        return f"{self.title} by {self.author}, published in {self.year}"

    def __repr__(self):
        #Return an official string representation that can recreate the Book instance.
        return f"Book('{self.title}', '{self.author}', {self.year})"

    def __del__(self):
        #Print a message when a Book instance is deleted.
        print(f"Deleting {self.title}")
