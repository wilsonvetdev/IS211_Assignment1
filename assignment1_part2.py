# Wilson Ng
# Spring 2021 - IS 211
# Python Version 3.9.1

class Book:

    def __init__(self, author = "", title = ""):
        self.author = author
        self.title = title 
    
    def display(self):
        print(f"{self.title}, written by {self.author}")
        
if __name__ == "__main__":
    first_book = Book("John Steinbeck", "Of Mice and Men")
    second_book = Book("Harper Lee", "To Kill a Mockingbird")
    first_book.display()
    second_book.display()



