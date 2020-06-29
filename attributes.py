class Person:
    name = "Harris"
    ID = "45960"
    number = "123-456-7890 "

    def getLoginInfo(self):
        entry_name = input("Enter your name here: ")
        entry_ID = input("Enter your ID# here: ")
        entry_number = input("Enter your Phone# here: ")
        if (entry_name == self.name and entry_ID == self.ID):
            print("Welcome back, {}!".format(entry_name))
        else:
            print("The ID# or name is incorrect.")

class Teacher(Person):
    salary = "33,000"
    ID = "Josh22"
    emp_num = "4583"

    def getLoginInfo(self):
        entry_name = input("Enter your name here: ")
        entry_ID = input("Enter your ID# here: ")
        entry_empnum = input("Enter you employee pin# here: ")
        if (entry_ID == self.ID and entry_empnum == self.empnum):
            print("Welcome back, {}!".format(entry_name))
        else:
            print("The employee number or ID is incorrect.")

class Student(Person):
    grade = "Junior"
    period = "1"
    password = "happy123"
    
    
    def getLoginInfo(self):
        entry_name = input("Enter your name here: ")
        entry_period = input("Enter your period# here: ")
        entry_password = input("Enter your password here: ")
        if (entry_period == self.period and entry_password == self.password):
            print("Welcome back, {}!".format(entry_name))
        else:
            print("The period number or password is incorrect.")


person = Person()
person.getLoginInfo()

teacher = Teacher()
teacher.getLoginInfo()

student = Student()
student.getLoginInfo()
