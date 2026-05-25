from sys import argv


try:
    assert len(argv) > 1, ""
except AssertionError:
    exit(1)

try:
    assert len(argv) == 2, "more than one argument is provided"

    try:
        argument = int(argv[1])
    except ValueError:
        raise AssertionError("argument is not an integer")

    if argument % 2 == 0:
        print("I'm Even.")
    else:
        print("I'm Odd.")

except AssertionError as error:
    print("AssertionError:", error.args[0])
