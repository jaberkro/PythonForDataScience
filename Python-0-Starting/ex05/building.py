import sys


def countText(textToCount):
    print("The text contains", len(textToCount), "characters")
    print(sum(1 for x in textToCount if x.isupper()), "upper letters")
    print(sum(1 for x in textToCount if x.islower()), "lower letters")
    print(sum(1 for x in textToCount if (
                                        x.isascii
                                        and not x.isupper()
                                        and not x.islower()
                                        and not x.isspace()
                                        and not x.isdigit()
                                    )), "punctuation marks")
    print(sum(1 for x in textToCount if x.isspace()), "spaces")
    print(sum(1 for x in textToCount if x.isdigit()), "digits")


def getUserInput():
    userInput = ""

    if len(sys.argv) == 2:
        userInput = sys.argv[1]

    while userInput == "":
        userInput = input("What is the text to count?\n")
        userInput += "\n"

    return userInput


def main():
    try:
        assert len(sys.argv) < 3, "more than one argument is provided"
    except AssertionError as error:
        print("AssertionError:", error.args[0])
        exit(1)

    userInput = getUserInput()
    countText(userInput)


if __name__ == "__main__":
    main()
