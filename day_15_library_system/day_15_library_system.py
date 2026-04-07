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
        # Return the title and year in one line.
        return f"Title: {self.title}, Year: {self.year}"


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
        # Return the title, year, and author on separate lines.
        return f"{super().get_info()}\nAuthor: {self.author}"


# This function checks if a title has only letters, numbers, spaces, and punctuation.
def is_valid_title(title):
    # Return True if title contains allowed characters only.
    return bool(TITLE_PATTERN.fullmatch(title))


# This function checks if the author name has only letters, spaces, and full stops.
def is_valid_author(author):
    # Return True if author contains allowed characters only.
    return bool(AUTHOR_PATTERN.fullmatch(author))


# This function asks a yes/no question and returns True for yes and False for no.
def ask_yes_no(prompt, reader=None, writer=None):
    reader = reader or input
    writer = writer or print

    # Keep asking until the user enters yes or no.
    while True:
        # Read user input and normalize it.
        answer = reader(prompt).strip().lower()
        # Return True for yes answers.
        if answer in ("yes", "y"):
            return True
        # Return False for no answers.
        if answer in ("no", "n"):
            return False
        # Show message for invalid yes/no input.
        writer("Please enter yes or no.")


# This function asks for title input and handles duplicate-title decisions.
def get_title_input(books, reader=None, writer=None):
    reader = reader or input
    writer = writer or print

    # Keep asking until the user enters a valid title or chooses to finish.
    while True:
        # Ask the user to type a book title.
        title = reader("Enter book title: ").strip()
        # Check if title is empty.
        if not title:
            # Show message if the title is empty.
            writer("Title cannot be empty.")
            continue
        # Check if title has invalid characters.
        if not is_valid_title(title):
            # Show message if title format is invalid.
            writer("Invalid title. Use only letters, numbers, spaces, and punctuation.")
            continue

        # Check whether this title already exists.
        is_duplicate = any(item.title.lower() == title.lower() for item in books)
        # Ask if user wants to continue with duplicate title.
        if is_duplicate:
            writer("Warning: This title is already submitted.")
            continue_duplicate = ask_yes_no(
                "Would you like to continue with this title? (yes/no): ",
                reader,
                writer,
            )
            # Ask for completion if user does not want to continue with duplicate title.
            if not continue_duplicate:
                done = ask_yes_no(
                    "Have you completed entering the data? (yes/no): ",
                    reader,
                    writer,
                )
                # End entry if the user confirms they are finished.
                if done:
                    return "", True
                # Ask for a different title if user is not done.
                continue

        # Return the valid title and continue flag.
        return title, False


# This function asks for publication year until the input is valid.
def get_year_input(reader=None, writer=None):
    reader = reader or input
    writer = writer or print

    # Keep asking for year until the user enters numbers only.
    while True:
        # Ask the user to type a publication year.
        year_input = reader("Enter publication year: ").strip()
        # Check if year input contains digits only.
        if not year_input.isdigit():
            # Show message for invalid year input.
            writer("Invalid year. Please enter numbers only.")
            continue
        # Convert valid year text to an integer and return it.
        return int(year_input)


# This function asks for author name until the input is valid.
def get_author_input(reader=None, writer=None):
    reader = reader or input
    writer = writer or print

    # Keep asking for author until the user enters a valid name.
    while True:
        # Ask the user to type the author's name.
        author = reader("Enter author name: ").strip()
        # Check if author input is empty.
        if not author:
            # Show message if author is empty.
            writer("Author cannot be empty.")
            continue
        # Check if author has invalid characters.
        if not is_valid_author(author):
            # Show message if author format is invalid.
            writer("Invalid author. Use only letters, spaces, and full stops.")
            continue
        # Return author when valid.
        return author


def collect_books(reader=None, writer=None):
    reader = reader or input
    writer = writer or print
    books = []

    while True:
        title, done = get_title_input(books, reader, writer)
        if done:
            return books

        year = get_year_input(reader, writer)
        author = get_author_input(reader, writer)
        books.append(Book(title, year, author))

        if ask_yes_no("Have you completed entering the data? (yes/no): ", reader, writer):
            return books


def format_books(books):
    lines = ["", "Books entered:"]
    for item in books:
        lines.append(item.get_info())
        lines.append("")
    return lines


# This function runs the complete data-entry process.
def main():
    books = collect_books()
    for line in format_books(books):
        print(line)


# This block runs only when this file is run directly.
if __name__ == "__main__":
    main()

# Run in terminal with: python day_15_library_system.py