Python 3.8.3 (tags/v3.8.3:6f8c832, May 13 2020, 22:20:19) [MSC v.1925 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> num1 = 4
>>> num1
4
>>> num2 = 5
>>> num2
5
>>> num3 = num1 + num2
>>> num3
9
>>> print(num1 + num2)
9
>>> num1 = 1.2
>>> num2 = 2.1
>>> myString = "hello world"
>>> myString
'hello world'
>>> len(myString)
11
>>> myString[0]
'h'
>>> myStrig[11]
Traceback (most recent call last):
  File "<pyshell#13>", line 1, in <module>
    myStrig[11]
NameError: name 'myStrig' is not defined
>>> myString[11]
Traceback (most recent call last):
  File "<pyshell#14>", line 1, in <module>
    myString[11]
IndexError: string index out of range
>>> myString[10]
'd'
>>> fName = "Grace"
>>> lName = "Arnsberger"
>>> print(fName + lName)
GraceArnsberger
>>> print(fName + " " + lName)
Grace Arnsberger
>>> print("Hello {} {}, welcome to Python!".format(fName,lName))
Hello Grace Arnsberger, welcome to Python!
>>> x = "My name is Grace"
>>> x
'My name is Grace'
>>> y = ("My last name" + "is Arnsberger")
>>> y
'My last nameis Arnsberger'
>>> y = ("My last name" + " " +"is Arnsberger")
>>> y
'My last name is Arnsberger'
>>> z = "My birthday is January 22"
>>> z
'My birthday is January 22'
>>> print(z[5:9])
rthd
>>> len(z)
25
>>> a = "Denver Colorado"
>>> print(string.strip('orad'))
Traceback (most recent call last):
  File "<pyshell#32>", line 1, in <module>
    print(string.strip('orad'))
NameError: name 'string' is not defined
>>> print(a.strip('orad'))
Denver Col
>>> b = a.upper()
>>> print(b)
DENVER COLORADO
>>> if "Denver" in a:
	print("yes")

	
yes
>>> txt = "I am 19 \"years\" old."
>>> print(txt)
I am 19 "years" old.
>>> num1 = "one"
>>> print(num1 + num2)
Traceback (most recent call last):
  File "<pyshell#42>", line 1, in <module>
    print(num1 + num2)
TypeError: can only concatenate str (not "float") to str
>>> num1
'one'
>>> num1 = "1"
>>> print(num1 + num2)
Traceback (most recent call last):
  File "<pyshell#45>", line 1, in <module>
    print(num1 + num2)
TypeError: can only concatenate str (not "float") to str
>>> print(int(num1) + num2)
3.1
>>> x + y
'My name is GraceMy last name is Arnsberger'
>>> c = "Kitten"
>>> a == b
False
>>> num2 < 20 and num2 < 15
True
>>> b is c
False
>>> a in b
False
>>> print(a & z)
Traceback (most recent call last):
  File "<pyshell#53>", line 1, in <module>
    print(a & z)
TypeError: unsupported operand type(s) for &: 'str' and 'str'
>>> num2 ~ num1
SyntaxError: invalid syntax
>>> (a | b)
Traceback (most recent call last):
  File "<pyshell#55>", line 1, in <module>
    (a | b)
TypeError: unsupported operand type(s) for |: 'str' and 'str'
>>> (int(num1) | num2)
Traceback (most recent call last):
  File "<pyshell#56>", line 1, in <module>
    (int(num1) | num2)
TypeError: unsupported operand type(s) for |: 'int' and 'float'
>>> animal = ( 'zebra', 'alligator', 'giraffe', 'goat', 'ox' )
>>> listofAnimals = list(animal)
>>> print(listofAnimals)
['zebra', 'alligator', 'giraffe', 'goat', 'ox']
>>> MyString = "I am from Denver Colorado"
>>> newString = list(MyString)
>>> print(newString)
['I', ' ', 'a', 'm', ' ', 'f', 'r', 'o', 'm', ' ', 'D', 'e', 'n', 'v', 'e', 'r', ' ', 'C', 'o', 'l', 'o', 'r', 'a', 'd', 'o']
>>> newString = MyString.split(" ")
>>> print(newString)
['I', 'am', 'from', 'Denver', 'Colorado']
>>> myList = [2, 3, 4]
>>> len(myList)
3
>>> for i in myList:
	print(i)

	
2
3
4
>>> myList[2]
4
>>> myList[0]
2
>>> myList.append(5)
>>> for i in myList:
	print(i)

	
2
3
4
5
>>> len(myList)
4
>>> print(myList)
[2, 3, 4, 5]
>>> newList = [8, 6, 4, 2]
>>> for i in newList:
	print(i)

	
8
6
4
2
>>> newList.append(0)
>>> newList
[8, 6, 4, 2, 0]
>>> lis2 = newList.copy()
>>> lis2
[8, 6, 4, 2, 0]
>>> print(lis2 + newList)
[8, 6, 4, 2, 0, 8, 6, 4, 2, 0]
>>> newList.reverse()
>>> print(newList)
[0, 2, 4, 6, 8]
>>> names = ( 'alex', 'zoe', 'harry', 'jesse', 'jace' )
>>> for i in names:
	print(i)

	
alex
zoe
harry
jesse
jace
>>> names.count()
Traceback (most recent call last):
  File "<pyshell#90>", line 1, in <module>
    names.count()
TypeError: count() takes exactly one argument (0 given)
>>> s = names.count()
Traceback (most recent call last):
  File "<pyshell#91>", line 1, in <module>
    s = names.count()
TypeError: count() takes exactly one argument (0 given)
>>> s = names.count()
Traceback (most recent call last):
  File "<pyshell#92>", line 1, in <module>
    s = names.count()
TypeError: count() takes exactly one argument (0 given)
>>> thistuple = (4, 6, 7, 4, 7, 5, 3)
>>> s = thistuple.count()
Traceback (most recent call last):
  File "<pyshell#94>", line 1, in <module>
    s = thistuple.count()
TypeError: count() takes exactly one argument (0 given)
>>> print(s)
Traceback (most recent call last):
  File "<pyshell#95>", line 1, in <module>
    print(s)
NameError: name 's' is not defined
>>> x = thistuple.count(5)
>>> print(x)
1
>>> myset = {"popcorn", "chips", "candy"}
>>> print(myset)
{'candy', 'popcorn', 'chips'}
>>> myset.add("fruit")
>>> print(myset)
{'candy', 'fruit', 'popcorn', 'chips'}
>>> myset.remove("popcorn")
>>> print(myset)
{'candy', 'fruit', 'chips'}
>>> newset = {"candy", "meat", "veggies"}
>>> j = newset.difference(myset)
>>> print(j)
{'meat', 'veggies'}
>>> myDictionary = {"index1": 1, "index2": 2, "index3": 355}
>>> myDictionary
{'index1': 1, 'index2': 2, 'index3': 355}
>>> myDictionary["index2"]
2
>>> dic_users = {"em_1234": {"fname": "bob", "lname": "smith", "phone":"123-67890"}, "em_1235": {"fname": "Mary" ,"lname": "Jones", "phone": "345-23490"} }
>>> print(dic_users["em_1235"])
{'fname': 'Mary', 'lname': 'Jones', 'phone': '345-23490'}
>>> print(dic_users["em_1235"]["phone"])
345-23490
>>> print
<built-in function print>
>>> print("User: {} {}\nPhone: {}".format(dic_users["em_1235"]["fname"],dic_users["em_1235"]["lname"],dic_users["em_1235"]["phone"]))
User: Mary Jones
Phone: 345-23490
>>> newDictionary = {"brand": "Gucci", "make": "sneakers", "year": "2020"}
>>> print(newdictionary)
Traceback (most recent call last):
  File "<pyshell#116>", line 1, in <module>
    print(newdictionary)
NameError: name 'newdictionary' is not defined
>>> print(newDictionary)
{'brand': 'Gucci', 'make': 'sneakers', 'year': '2020'}
>>> x = newDictionary.get("brand")
>>> print(x)
Gucci
>>> newDictionary.update({"year": "2021"})
>>> print(newDictionary)
{'brand': 'Gucci', 'make': 'sneakers', 'year': '2021'}
>>> newDictionary.update({"color": "hot pink"})
>>> print(newDictionary)
{'brand': 'Gucci', 'make': 'sneakers', 'year': '2021', 'color': 'hot pink'}
>>> dic_people = {"Person1": {"fname": "lily", "lname": "coleman", "phone":"394-72038"}, "Person2": {"fname": "Sharon" ,"lname": "Kincl", "phone": "847-74928"} }
>>> x = ('key1', 'key2', 'key3')
>>> y = 0
>>> thisdict = dict.fromkeys(x, y)
>>> print(thisdict)
{'key1': 0, 'key2': 0, 'key3': 0}
>>> b = [3, 6, 9]
>>> "Hello World"
'Hello World'
>>> name = "Bob"
>>> print(name)
Bob
>>> name = "Python"
>>> print(type(name))
<class 'str'>
>>> answer = True
>>> type(answer)
<class 'bool'>
>>> answer = False
>>> type(answer)
<class 'bool'>
>>> a = 30
>>> b = 3
>>> if b > a:
	print("b is greater than a")
    else:
	    
SyntaxError: unindent does not match any outer indentation level
>>> if b > a:
	print("b is greater than a")
	else:
		
SyntaxError: invalid syntax
>>> if b > a:
	print("b is greater than a")
else:
	print("b is not greater than a")

	
b is not greater than a
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

help> modules

Please wait a moment while I gather a list of all available modules...

__future__          asyncio             history             sched
__main__            asyncore            hmac                scrolledlist
_abc                atexit              html                search
_ast                audioop             http                searchbase
_asyncio            autocomplete        hyperparser         searchengine
_bisect             autocomplete_w      idle                secrets
_blake2             autoexpand          idle_test           select
_bootlocale         base64              idlelib             selectors
_bz2                bdb                 imaplib             setuptools
_codecs             binascii            imghdr              shelve
_codecs_cn          binhex              imp                 shlex
_codecs_hk          bisect              importlib           shutil
_codecs_iso2022     browser             inspect             sidebar
_codecs_jp          builtins            io                  signal
_codecs_kr          bz2                 iomenu              site
_codecs_tw          cProfile            ipaddress           smtpd
_collections        calendar            itertools           smtplib
_collections_abc    calltip             json                sndhdr
_compat_pickle      calltip_w           keyword             socket
_compression        cgi                 lib2to3             socketserver
_contextvars        cgitb               linecache           sqlite3
_csv                chunk               locale              squeezer
_ctypes             cmath               logging             sre_compile
_ctypes_test        cmd                 lzma                sre_constants
_datetime           code                macosx              sre_parse
_decimal            codecontext         mailbox             ssl
_dummy_thread       codecs              mailcap             stackviewer
_elementtree        codeop              mainmenu            stat
_functools          collections         marshal             statistics
_hashlib            colorizer           math                statusbar
_heapq              colorsys            mimetypes           string
_imp                compileall          mmap                stringprep
_io                 concurrent          modulefinder        struct
_json               config              msilib              subprocess
_locale             config_key          msvcrt              sunau
_lsprof             configdialog        multicall           symbol
_lzma               configparser        multiprocessing     symtable
_markupbase         contextlib          netrc               sys
_md5                contextvars         nntplib             sysconfig
_msi                copy                nt                  tabnanny
_multibytecodec     copyreg             ntpath              tarfile
_multiprocessing    crypt               nturl2path          telnetlib
_opcode             csv                 numbers             tempfile
_operator           ctypes              opcode              test
_osx_support        curses              operator            textview
_overlapped         dataclasses         optparse            textwrap
_pickle             datetime            os                  this
_py_abc             dbm                 outwin              threading
_pydecimal          debugger            parenmatch          time
_pyio               debugger_r          parser              timeit
_queue              debugobj            pathbrowser         tkinter
_random             debugobj_r          pathlib             token
_sha1               decimal             pdb                 tokenize
_sha256             delegator           percolator          tooltip
_sha3               difflib             pickle              trace
_sha512             dis                 pickletools         traceback
_signal             distutils           pip                 tracemalloc
_sitebuiltins       doctest             pipes               tree
_socket             dummy_threading     pkg_resources       tty
_sqlite3            dynoption           pkgutil             turtle
_sre                easy_install        platform            turtledemo
_ssl                editor              plistlib            types
_stat               email               poplib              typing
_statistics         encodings           posixpath           undo
_string             ensurepip           pprint              unicodedata
_strptime           enum                practice            unittest
_struct             errno               profile             urllib
_symtable           faulthandler        pstats              uu
_testbuffer         filecmp             pty                 uuid
_testcapi           fileinput           py_compile          venv
_testconsole        filelist            pyclbr              warnings
_testimportmultiple fnmatch             pydoc               wave
_testmultiphase     format              pydoc_data          weakref
_thread             formatter           pyexpat             webbrowser
_threading_local    fractions           pyparse             window
_tkinter            ftplib              pyshell             winreg
_tracemalloc        functools           query               winsound
_warnings           gc                  queue               wsgiref
_weakref            genericpath         quopri              xdrlib
_weakrefset         getopt              random              xml
_winapi             getpass             re                  xmlrpc
_xxsubinterpreters  gettext             redirector          xxsubtype
abc                 glob                replace             zipapp
aifc                grep                reprlib             zipfile
antigravity         gzip                rlcompleter         zipimport
argparse            hashlib             rpc                 zlib
array               heapq               run                 zoomheight
ast                 help                runpy               zzdummy
asynchat            help_about          runscript           

Enter any module name to get more help.  Or, type "modules spam" to search
for modules whose name or summary contain the string "spam".

help> quit 

You are now leaving help and returning to the Python interpreter.
If you want to ask for help on a particular object directly from the
interpreter, you can type "help(object)".  Executing "help('string')"
has the same effect as typing a particular string at the help> prompt.
>>> 
>>> 
>>> 
>>> 
>>> import math
>>> math.floor(3.5)
3
>>> 