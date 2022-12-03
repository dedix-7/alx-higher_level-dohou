This file contains some personal jottings for Python:

-c cmd -> Run Python script sent in as cmd string.


-d -> It provides debug output.


-O -> It generates optimized bytecode (resulting in .pyo files).


-v -> verbose output (detailed trace on import statements).


echo $? tells us the exit status code.


The type() is a function used to determine the data type of a given value. 
An example of a use case is:
	>>> type("Hello, World")
	<class 'str'>


.isidentifier() function tells us if a string is a valid identifier. 
Example of a use case:
	>>> 'name'.isientifier()
	True


The len() function allows you to check for the length of a string, or the length of a string assigned to a variable. 
Example 1: 	>>> text = "Hello World"
		>>> len(text)
		11
Example 2: 	>>> len("abc")
		3


To deal with multiline strings, you can break them up accross multiple lines into multiple strings.
Example:  >>> dan = "I am \
		....the Flash."
	>>> print(dan)
	I am the Flash.


Multiline strings in Python work just the same way in Kotlin: using triple quotes ( """""" or '''''')
Example:  >>> paragraph = """This planet has—or rather had—a problem, which was
	this: most of the people living on it were unhappy for pretty much
	of the time. Many solutions were suggested for this problem, but
	most of these were largely concerned with the movements of small
	green pieces of paper, which is odd because on the whole it wasn't
	the small green pieces of paper that were unhappy."""
	>>> print(paragraph)
	This planet has—or rather had—a problem, which was
	this: most of the people living on it were unhappy for pretty much
	of the time. Many solutions were suggested for this problem, but
	most of these were largely concerned with the movements of small
	green pieces of paper, which is odd because on the whole it wasn't
	the small green pieces of paper that were unhappy.



