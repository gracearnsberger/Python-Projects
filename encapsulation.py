class Protected:
    def __init__(self):
        self._protectVar = 0

obj = Protected()
obj._protectVar = 34
print(obj._protectVar)



class Private:
    def __init__(self):
        self.__privateVar = 12
    def getPrivate(self):
        print(self.__privateVar)
    def setPrivate(self, private):
        self.__privateVar = private

obj = Private()
obj.getPrivate()
