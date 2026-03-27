# Here we are defininfng a variable called new_score and assigning it the value of 150.
new_score = 150

def main():
    # "with" is a context manager that allows us to work with files.
    # "open" is a function that opens a file and returns a file object. We are opening a file called "high_score.txt" in write mode ("w").
    # "as" is used to assign the file object to a variable called "file". This allows us to work with the file object within the block of code.
    with open("high_score.txt", "w") as file:
        # "write" is a method of the file object that allows us to write data to the file.
        # "str" is a function that converts the new_score variable to a string, since the write method expects a string argument.
        file.write(str(new_score))

    # Immediately after writing the new score to the file, open the same file, read the value back and print "The saved high score is: [new_score]".
    # "open" is used again to open the file in read mode ("r").
    with open("high_score.txt", "r") as file:
        # "read" is a method of the file object that reads the contents of the file and returns it as a string. We are storing this value in a variable called "saved_score".
        saved_score = file.read()
        # Print the saved high score.
        print(f"The saved high score is: {saved_score}")


if __name__ == "__main__":
    main()


# script to run: python high_score_tracker.py