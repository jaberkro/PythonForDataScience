def all_thing_is_obj(object: any) -> int:
    """This function prints the type of the object if it is a list, tuple, \
        set, dict or string. In the specific case of string, it prints an \
        extra 'is in the kitchen' message to match the subject requirement"""
    match object:
        case list():
            print("List : ", type(object))
        case tuple():
            print("Tuple :", type(object))
        case set():
            print("Set :", type(object))
        case dict():
            print("Dict :", type(object))
        case str():
            print(object, "is in the kitchen :", type(object))
        case _:
            print("Type not found")

    return 42
