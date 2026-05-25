from sys import argv
from ft_filter import ft_filter


def main() -> int:
    """Program to print all words from an input S that are bigger than N \
    characters long. Usage: python3 filterstring.py \"S\" N"""
    S = []
    N = 0

    try:
        assert len(argv) == 3, "the arguments are bad"

        try:
            S = (argv[1]).split()
            N = int(argv[2])
        except ValueError:
            raise AssertionError("the arguments are bad")

        print(ft_filter(lambda word: len(word) > N, S))

    except AssertionError as error:
        print("AssertionError:", error.args[0])
        return 1
    return 0


if __name__ == "__main__":
    main()
