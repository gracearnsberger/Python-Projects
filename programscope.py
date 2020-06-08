Python 3.7.5 (tags/v3.7.5:5c02a39a0b, Oct 15 2019, 00:11:34) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> name = "Python"
>>> 
>>> def getName():
	print("I am coding with().format(name))
	      
SyntaxError: EOL while scanning string literal
>>> def getName():
	print("I am coding with()".format(name))

>>> getName()
I am coding with()
>>> 
def getName():
	name = "C#"
	print("I am coding with()".format(name))

	
>>> getName()
I am coding with()
>>> def getName():
	name = "C#"
	print("I am coding with()".format(name) )

	
>>> getName()
I am coding with()
>>> import sys
>>> import monket
Traceback (most recent call last):
  File "<pyshell#14>", line 1, in <module>
    import monket
ModuleNotFoundError: No module named 'monket'
>>> fName = input("What is your first name?")
What is your first name?
>>> fName = input("What is your first name?\n>>> ")
What is your first name?
>>> grace
>>> fName = input("What is your \"first name?\n>>> ")
What is your "first name?
>>> fName = input("What is your \"first name\"?\n>>> ")
>>> 
>>> #This is my note.

================================ RESTART: Shell ================================
>>> 
