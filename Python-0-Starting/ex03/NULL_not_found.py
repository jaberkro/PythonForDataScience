def NULL_not_found(object: any) -> int:
    """This function prints the type of the different objects when the value \
    is NULL or similar. In the case of Float, the word 'Cheese' is printed \
    instead of 'float' to match the subject requirement"""
    match object:
        case None:
            print("Nothing:", object, type(object))
        case float():
            print("Cheese:", object, type(object))
        case False:
            print("Fake:", object, type(object))
        case 0:
            print("Zero:", object, type(object))
        case "":
            print("Empty:", type(object))
        case _:
            print("Type not found")
            return 1

    return 0
