Python 3.8.3 (tags/v3.8.3:6f8c832, May 13 2020, 22:20:19) [MSC v.1925 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> myString = "hello world"
>>> myString
'hello world'
>>> len(myString)
11
>>> myString[0]
'h'
>>> myString[1]
'e'
>>> fName = "Grace"
>>> lName = "Arnsberger"
>>> print(fName + lName)
GraceArnsberger
>>> print(fName + " "+  lName)
Grace Arnsberger
>>> print("Hello {} {} , welcome to Python!".format(fName,lName))
Hello Grace Arnsberger , welcome to Python!
>>> txt = "For only {price:.2f} dollars!"
print(txt.format(price = 22))
SyntaxError: multiple statements found while compiling a single statement
>>> txt = "For only {price:.2f} dollars!"

>>> print(txt.format(price = 22))
For only 22.00 dollars!
>>> x = format(0.22, '%')

>>> print(x)
22.000000%
>>> def getSum(num1,num2):
	answer: = num1 + num2
	
SyntaxError: invalid syntax
>>> def getSum(num1,num2):
	answer = num1 + num2
	print("The answer is {}.".format(answer))

	
>>> getSum(2,4)
The answer is 6.
>>> myAdd = getSum
>>> myAdd(2, 4)
The answer is 6.
>>> help()

Welcome to Python 3.8's help utility!

If this is your first time using Python, you should definitely check out
the tutorial on the Internet at https://docs.python.org/3.8/tutorial/.

Enter the name of any module, keyword, or topic to get help on writing
Python programs and using Python modules.  To quit this help utility and
return to the interpreter, just type "quit".

To get a list of available modules, keywords, symbols, or topics, type
"modules", "keywords", "symbols", or "topics".  Each module also comes
with a one-line summary of what it does; to list the modules whose name
or summary contain a given string such as "spam", type "modules spam".

help> 