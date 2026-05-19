
class Person:
    def __init__(self, name, age, id, salary):
        self.name = name
        self.age = age
        self.id = id
        self.salary = salary

    def setdata(self, name, age, id, salary):
        self.name = name
        self.age = age
        self.id = id
        self.salary = salary

    def set_name(self,name):
        self.name = name

    def set_age(self,age):
        self.age = age

    def set_id(self,id):
        self.id = id

    def set_salary(self,salary):
        self.salary = salary

    def getdata(self):
        print(f"The name is: {self.name}, id is: {self.id}, age is: {self.age}, salary is: {self.salary}")

class Employee(Person):
    def __init__(self, name, age, __id, __salary, hr, finance):
        self.hr = hr
        self.finance = finance
        super().__init__(name, age, __id, __salary)


    def set_hr(self, hr):
            self.hr = hr

    def set_finance(self, finance):
            self.finance = finance
        
    def getdata(self):
        print(f"The name is: {self.name}, age is: {self.age}, id is: {self.id}, salary is: {self.salary}, hr is: {self.hr}, finance is: {self.finance}")

class Manager(Person):
    def __init__(self, name, age, id, salary, language):
        self.language = language
        super().__init__(name, age, id, salary)

    def set_language(self, language):
        self.language = language


    def getdata(self):
        print(f"The name is: {self.name}, age is: {self.age}, id is: {self.id}, salary is: {self.salary}, language is: {self.language}")

persons = []
managers = []
employees = []

while True:

    print("Welcome to the bank!")

    print("Enter 1. to add person:")
    print("Enter 2. to add employee:")
    print("Enter 3. to add manager:")
    print("Enter 4. to see the details:")
    print("Enter 0. to exit:\n")

    choice = int(input("Enter your choice:\n"))

    if choice == 1:
        name = input("Enter your name: ")
        age = int(input("Enter your age: "))
        id = int(input("Enter your id: "))
        salary = int(input("Enter your salary: "))

        pobj = Person(name, age, id, salary)
        persons.append(pobj)

    elif choice == 2:

        name = input("Enter your name: ")
        age = int(input("Enter your age: "))
        id = int(input("Enter your id: "))
        salary = int(input("Enter your salary: "))
        hr = input("Enter your hr: ")
        finance = input("Enter your finance: ")

        eobj = Employee(name, age, id, salary, hr, finance)
        employees.append(eobj)
    elif choice == 3:

        name = input("Enter your name: ")
        age = int(input("Enter your age: "))
        id = int(input("Enter your id: "))
        salary = int(input("Enter your salary: "))
        language = input("Enter your programming language: ")

        mobj = Manager(name, age, id, salary, language)
        managers.append(mobj)
    elif choice == 4:
        print("Choose details to show:\n")

        print("Enter 1. for person details:")
        print("Enter 2. for employee details:")
        print("Enter 3. for manager details:")

        num = int(input("Enter your choice: "))

        if num == 1:
            for person in persons:
                person.getdata()

        elif num == 2:
            for employee in employees:
                employee.getdata()

        elif num == 3:
            for manager in managers:
                manager.getdata()

    elif choice == 0:
        print("THANK YOU!")
        break

    else:
        print("Your choice is not valid")
