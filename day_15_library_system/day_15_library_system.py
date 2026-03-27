import re


# Store regex patterns once so they are not recompiled on every function call.
TITLE_PATTERN = re.compile(r"[A-Za-z0-9\s\.,!\?;:'\"\-()\[\]{}_/&]+")
AUTHOR_PATTERN = re.compile(r"[A-Za-z.\s]+")


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


# This function checks if a title has only letters, numbers, spaces, and punctuation.
def is_valid_title(title):
    # Return True if title contains allowed characters only.
    return bool(TITLE_PATTERN.fullmatch(title))


# This function checks if the author name has only letters, spaces, and full stops.
def is_valid_author(author):
    # Return True if author contains allowed characters only.
    return bool(AUTHOR_PATTERN.fullmatch(author))


# This function asks a yes/no question and returns True for yes and False for no.
def ask_yes_no(prompt):
    # Keep asking until the user enters yes or no.
    while True:
        # Read user input and normalize it.
        answer = input(prompt).strip().lower()
        # Return True for yes answers.
        if answer in ("yes", "y"):
            return True
        # Return False for no answers.
        if answer in ("no", "n"):
            return False
        # Show message for invalid yes/no input.
        print("Please enter yes or no.")


# This function asks for title input and handles duplicate-title decisions.
def get_title_input(books):
    # Keep asking until the user enters a valid title or chooses to finish.
    while True:
        # Ask the user to type a book title.
        title = input("Enter book title: ").strip()
        # Check if title is empty.
        if not title:
            # Show message if the title is empty.
            print("Title cannot be empty.")
            continue
        # Check if title has invalid characters.
        if not is_valid_title(title):
            # Show message if title format is invalid.
            print("Invalid title. Use only letters, numbers, spaces, and punctuation.")
            continue

        # Check whether this title already exists.
        is_duplicate = any(item.title.lower() == title.lower() for item in books)
        # Ask if user wants to continue with duplicate title.
        if is_duplicate:
            print("Warning: This title is already submitted.")
            continue_duplicate = ask_yes_no(
                "Would you like to continue with this title? (yes/no): "
            )
            # Ask for completion if user does not want to continue with duplicate title.
            if not continue_duplicate:
                done = ask_yes_no("Have you completed entering the data? (yes/no): ")
                # End entry if the user confirms they are finished.
                if done:
                    return "", True
                # Ask for a different title if user is not done.
                continue

        # Return the valid title and continue flag.
        return title, False


# This function asks for publication year until the input is valid.
def get_year_input():
    # Keep asking for year until the user enters numbers only.
    while True:
        # Ask the user to type a publication year.
        year_input = input("Enter publication year: ").strip()
        # Check if year input contains digits only.
        if not year_input.isdigit():
            # Show message for invalid year input.
            print("Invalid year. Please enter numbers only.")
            continue
        # Convert valid year text to an integer and return it.
        return int(year_input)


# This function asks for author name until the input is valid.
def get_author_input():
    # Keep asking for author until the user enters a valid name.
    while True:
        # Ask the user to type the author's name.
        author = input("Enter author name: ").strip()
        # Check if author input is empty.
        if not author:
            # Show message if author is empty.
            print("Author cannot be empty.")
            continue
        # Check if author has invalid characters.
        if not is_valid_author(author):
            # Show message if author format is invalid.
            print("Invalid author. Use only letters, spaces, and full stops.")
            continue
        # Return author when valid.
        return author


# This function runs the complete data-entry process.
def main():
    # Create an empty list to store all book objects.
    books = []

    # Keep asking for books until the user says they are done.
    while True:
        # Ask for title and determine whether the user chose to finish.
        title, done = get_title_input(books)
        # Stop the loop if user chose to finish while in duplicate-title flow.
        if done:
            break

        # Ask for valid year and author details.
        year = get_year_input()
        author = get_author_input()

        # Create a Book object from the user input.
        book = Book(title, year, author)
        # Add the new book object to the list.
        books.append(book)

        # Ask if the user is finished entering data.
        done = ask_yes_no("Have you completed entering the data? (yes/no): ")
        # Stop the loop if the user says yes.
        if done:
            break

    # Print a heading before showing all entered books.
    print("\nBooks entered:")
    # Loop through every book in the list.
    for item in books:
        # Print each book's information.
        item.get_info()
        # Print a blank line for readability.
        print()


# This block runs only when this file is run directly.
if __name__ == "__main__":
    main()

# Run in terminal with: python day_15_library_system.py