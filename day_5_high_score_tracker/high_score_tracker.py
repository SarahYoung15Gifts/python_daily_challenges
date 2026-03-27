from pathlib import Path


# Here we are defininfng a variable called new_score and assigning it the value of 150.
new_score = 150
HIGH_SCORE_PATH = Path(__file__).with_name("high_score.txt")


def save_high_score(path, score):
    with path.open("w") as file:
        file.write(str(score))


def load_high_score(path):
    with path.open("r") as file:
        return file.read()


def format_high_score_message(score):
    return f"The saved high score is: {score}"

def main():
    save_high_score(HIGH_SCORE_PATH, new_score)
    saved_score = load_high_score(HIGH_SCORE_PATH)
    print(format_high_score_message(saved_score))


if __name__ == "__main__":
    main()


# script to run: python high_score_tracker.py