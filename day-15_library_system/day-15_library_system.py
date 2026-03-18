# This class is the base class for all library items.
class LibraryItem:
    # This runs when a new LibraryItem object is created.
    def __init__(self, title, year):
        # Save the title value to the object.
        self.title = title
        # Save the year value to the object.
        self.year = year

    # This method prints the basic item information.
    def get_info(self):
        # Print the title and year in one line.
        print(f"Title: {self.title}, Year: {self.year}")


# This class represents a book and inherits from LibraryItem.
class Book(LibraryItem):
    # This runs when a new Book object is created.
    def __init__(self, title, year, author):
        # Call the parent class setup for title and year.
        super().__init__(title, year)
        # Save the author value to the object.
        self.author = author

    # This method prints book information.
    def get_info(self):
        # Print the title and year from the parent class method.
        super().get_info()
        # Print the author on a new line.
        print(f"Author: {self.author}")


# This block runs only when this file is run directly.
if __name__ == "__main__":
    # Create a Book object with title, year, and author.
    book = Book("The Great Gatsby", 1925, "F. Scott Fitzgerald")
    # Call get_info to print the book details.
    book.get_info()

# Run in terminal with: python day-15_library_system.py