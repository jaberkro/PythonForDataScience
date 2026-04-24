def NULL_not_found(object: any) -> int:
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