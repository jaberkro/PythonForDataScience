from sys import argv
from string import punctuation as punct


def countText(text: str) -> None:
    """Prints the total count of characters and count per type for a string"""
    print("The text contains", len(text), "characters")
    print(sum(1 for char in text if char.isupper()), "upper letters")
    print(sum(1 for char in text if char.islower()), "lower letters")
    print(sum(1 for char in text if char in punct), "punctuation marks")
    print(sum(1 for char in text if char.isspace()), "spaces")
    print(sum(1 for char in text if char.isdigit()), "digits")


def getUserInput() -> str:
    """Takes the input argument from the user, or prompts the user to \
        give one if it was not provided or empty"""
    userInput = ""

    if len(argv) == 2:
        userInput = argv[1]

    while userInput == "":
        userInput = input("What is the text to count?\n")
        userInput += "\n"

    return userInput


def main() -> int:
    """Program to print the total character count of an inputted string, \
        as well as the count per type of characters"""
    try:
        assert len(argv) < 3, "more than one argument is provided"
    except AssertionError as error:
        print("AssertionError:", error.args[0])
        return 1

    userInput = getUserInput()
    countText(userInput)

    return 0


if __name__ == "__main__":
    main()
