mySentence = "loves the color"

color_list = ["red", "blue", "green", "pink", "teal", "black"]

def color_function(name) :
    lst = [ ]
    for i in color_list:
        msg = "{0}  {1} {2}".format(name,mySentence,i)
        lst.append(msg)
    return lst

def get_name() :
    go = True
    while go:
        name = input("What is your name? ")
        if name == "":
            print("You need to provide your name!")
        elif name == "grace":
            print("Grace you may not use this software.")
        else:
            go = False
    lst = color_function(name)
    for i in lst:
        print(i)
        
get_name()


def my_function():
    print("Grace's Function!!!")

my_function()

seasons = ["winter", "fall", "summer", "spring"]

x = seasons

for x in seasons:
    print(x)


x = seasons.count("summer")

print(x)

seasons.sort()
print(seasons)

x = lambda a, b : a * b
print(x(5, 6))

myString = "hello world"
myString
