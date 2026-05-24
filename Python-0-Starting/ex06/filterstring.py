import sys
from ft_filter import ft_filter


def main():
    """Program to print all words from an input S that are bigger than N \
    characters long. Usage: python3 filterstring.py \"S\" N"""
    S = []
    N = 0

    try:
        assert len(sys.argv) == 3, "the arguments are bad"

        try:
            S = (sys.argv[1]).split()
            N = int(sys.argv[2])
        except ValueError:
            raise AssertionError("the arguments are bad")

        print(ft_filter(lambda word: len(word) > N, S))

    except AssertionError as error:
        print("AssertionError:", error.args[0])
        exit(1)


if __name__ == "__main__":
    main()
