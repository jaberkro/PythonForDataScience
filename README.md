# PythonForDataScience
Folder to store my code for the 'Python for data science' piscine at Codam Coding College. This python piscine is part of the Advanced Curriculum and a preparation to move towards the artificial intelligence-related projects

This piscine has 5 modules, which each have their own exercises. In this README I will summarize the challenges and my approach to tackle them:

### Python-0-Starting
#### ex00
This exercise is about getting to know the different data types that are commonly used in Python: List, Tuple, Set and Dictionary. The challenge is to change the second element (index 1) of each predefined data type. Changing data in a List is easily done by overwriting the data at the specific index, but Tuples are a bit more tricky because they are unchangeable. The only way to change the data in a tuple is be redefining the data. For a Set you can discard elements and add them, but they will be added to the front of the Set, potentially messing up the order. For Dictionaries you can re-assign a value to a specific key.

#### ex01
This exercise is about printing and formatting date time information. In my implementation I worked with F-strings and time.strftime.

#### ex02
This exercise is about identifying the type of an object, which can be simply done with the type() function. However, simply using this and returning does not give the expected output. To create the expected output, I used a switch case, that will type a bit of extra information if it is a specific type. For integers, we print 'type not found', even though it is possible to find the type of an integer.