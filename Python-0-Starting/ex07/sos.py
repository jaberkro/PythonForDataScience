import sys


def getNestedMorse():
    """function that returns a dictionary with morse codes for chars, digits \
        and spaces"""
    NESTED_MORSE = {" ": "/ ",
                    "A": ".- ",
                    "B": "-... ",
                    "C": "-.-. ",
                    "D": "-.. ",
                    "E": ". ",
                    "F": "..-. ",
                    "G": "--. ",
                    "H": ".... ",
                    "I": ".. ",
                    "J": ".--- ",
                    "K": "-.- ",
                    "L": ".-.. ",
                    "M": "-- ",
                    "N": "-. ",
                    "O": "--- ",
                    "P": ".--. ",
                    "Q": "--.- ",
                    "R": ".-. ",
                    "S": "... ",
                    "T": "- ",
                    "U": "..- ",
                    "V": "...- ",
                    "W": ".-- ",
                    "X": "-..- ",
                    "Y": "-.-- ",
                    "Z": "--.. ",

                    "0": "----- ",
                    "1": ".---- ",
                    "2": "..--- ",
                    "3": "...-- ",
                    "4": "....- ",
                    "5": "..... ",
                    "6": "-.... ",
                    "7": "--... ",
                    "8": "---.. ",
                    "9": "----. "
                    }

    return NESTED_MORSE


def main():
    """Program that converts a given input text to morse"""
    try:
        nestedMorse = getNestedMorse()
        morseOutput = ""

        assert len(sys.argv) == 2, "the arguments are bad"

        for char in sys.argv[1]:
            assert char.isspace() or char.isalnum(), "the arguments are bad"

        for char in sys.argv[1]:
            morseOutput += nestedMorse[char.upper()]
        print(morseOutput[:-1])

    except AssertionError as error:
        print("AssertionError:", error.args[0])
        exit(1)


if __name__ == "__main__":
    main()
