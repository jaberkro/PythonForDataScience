import sys

try:
    assert len(sys.argv) > 1, ""
except AssertionError:
    sys.exit()

try:
    assert len(sys.argv) == 2, "more than one argument is provided"

    try:
        argument = int(sys.argv[1])
        
        if argument % 2 == 0:
            print("I'm Even.")
        else:
            print("I'm Odd.")
    except:
        raise AssertionError("argument is not an integer")
except AssertionError as error:
    print("AssertionError:", error.args[0])
