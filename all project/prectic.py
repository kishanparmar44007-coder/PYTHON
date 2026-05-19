# student = []

# while True:

#     print("welcome to the student list !\n")

#     print("1. student add :")
#     print("2. student update :")
#     print("3. student delet :")
#     print("4. student read :")
#     print("0. exit :")

#     choies=int(input("enter your choice :"))

#     if choies==1:
#         st={
#             "id" : int(input("enter student id :")),
#             "name" : input("enter student name :"),
#             "age" : int(input("enter student age :")),
#             "city" : input("enter student city :")
#         }

#         student.append(st)

#     elif choies==2:
#         id=int(input("enter studetn id for update :"))
#         for st in student:
#             if st["id"]==id:
#                 st["name"]==input("enter student name :")
#                 st["age"]==int(input("enter student age ;"))
#                 st["city"]==input("enter city :")
                
#     elif choies==3:
#         id=int(input("enter student id for delet :"))
#         for st in student:
#             if st["id"]==id:
#                 student.remove(st)

#     elif choies==4:
#         id=int(input("enter st id :"))
#         for st in student:
#             if st["id"]==id:
#                 print(f"student name {st["name"]}")
#                 print(f"student age{st["age"]}")
#                 print(F"student city{st["city"]}")

#     elif choies==0:
#         print("thank you !")
#         break

#     else:
#         print("your  choice is not here in list :")


# student = []

# while True:

#     print("welcome to the school list :")

#     print("Select an option:")

#     print("1. Add student")
#     print("2. Dispiay all Student")
#     print("3. updete student Information")
#     print("4. Del(et Student")
#     print("5. Display subjects offered")
#     print("6. Exit\n")

#     choice=int(input("Enetr your choice:"))

#     if choice==1:
#         sh={
#             "id" : tuple(input("enter st id :")),
#             "name" : input("enter st name :"),
#             "age" : int(input("enter st age :")),
#             "grade" : input("enter st grade :"),
#             "dob" : tuple(input("enter st dob :")),
#             "subject" : input("enter st subject :")
#         }

#         student.append(sh)

#     elif choice==2:
#         id=(input("enter st id :"))
#         for sh in student:
#             print("hi")
#             if sh["id"][0]==id:
#                 print(f"name :{sh["name"]}| age:{sh["age"]}| grade:{sh["grade"]}| dob:{sh["dob"]}| subject:{sh["subject"]}|")
        
#     elif choice==3:
#         id=(input("enter st id :"))
#         for sh in student:
#             if sh["id"][0]==id:
#                 sh["name"]=input("enter st name :")
#                 sh["age"]=int(input("enter st age :"))
#                 sh["grade"]=input("enter st grade :")
#                 sh["dob"]=(input("enter st dob :"))
#                 sh["subject"]=input("enter st subject :")
#             else:
#                 print("no")

#     elif choice==4:
#         id=(input("enter st id :"))
#         for sh in student:
#             if sh["id"][0]==id:
#                 del sh
#             print("the student deleted !")

#     elif choice==5:
#         id=(input("enter st id :"))
#         for sh in student:
#             print("hi")
#             if sh["id"][0]==id:
#                 print(f"student subject {sh["subject"]}")

#     elif choice==6:
#         print("thank you !")
#         break

#     else:
#         print("your choice is not this list !")


# while True:
#     print("Wlcome to the patter Generator and Number Analyzer!")

#     print()

#     print("1. generate a Pattern")
#     print("2. Analyze a Range of Number")
#     print("3. Exit")

#     choice=int(input("Enter your choice:"))

#     if choice==1:
#         ranges=int(input("enter range fo pattern :"))
#         for i in range(1,ranges+1):
#             print("*"*i)
#             print("your pattern !")

#     elif choice==2:p
#         s=int(input("enter number for start range :"))
#         e=int(input("enter number for end range :"))
#         all=0

#         for P in range(s+e+1):
            
#             if P %2==0:
#                 print("iv")

#             else:
#                 print("od")
#             all+=P

#         print(f"sum fo all value {s} to {e} is {all}")

#     elif choice==3:
#         print("thank you !")
#         break
        
        

#     else:
#         print("thus number is not for list !")



# class car:
#     barnd = "bmw"
#     modle = "m1"
#     price = 200000

# car1 = car()

# print(car1.barnd,car1.modle,car1.price)

# class car:
#     def __init__(self,brand,model):
#         self.brand=brand
#         self.model=model
        
#     def set_brand(self,brand):
#         self.brand=brand

#     def get_brand(self):
#         return self.brand

# car1=car("toyota","coroll")

# print(car1.get_brand()) 
# car1.set_brand("honda")
# print(car1.get_brand())

class Persons:
    def __init__(self,id,name ,age,salary):
        self.id = id
        self.name = name
        self.age = age 
        self.salary = salary

    def setdata(self,id,name,age,salary):
        self.id = id
        self.name = name
        self.age = age
        self.salary = salary

    def set_id(self,id):
        self.id = id

    def set_name(self,name):
        self.name = name

    def set_age(self,age):
        self.age = age

    def set_salary(self,salary):
        self.salary = salary

    def getdata(self):
        print(f"Employee name : {self.name} | and age {self.age}")

class employee(Persons):
    def __init__(self, __id, name, age, __salary,hr,finance):
        self.hr == hr
        self.finance = finance
        super().__init__(__id, name, age, __salary)

    def set_hr(self,hr):
        self.hr =hr

    def set_finance(self,finance):
        self.finance = finance

    def getdata(self):
        print(f"employee name : {self.name} | age : {self.age} | id : {self.id}")

class manager(employee):
    def __init__(self, id,  name, age, salary, hr, finance,language):
        self.language = language
        super().__init__(id, name, age, salary, hr, finance)

    def set_language(self,language):
        self.language = language

    def getdata(self):
        print(f"manager name :{self.name} | age : {self.age} | id : {self.id} | salary : {self.salary}")

Persons_ilst = []
employee_list = []
manager_list = []

while True:
    
    print("Welcome to the bank!")

    print("Enter 1. to add person:")
    print("Enter 2. to add employee:")
    print("Enter 3. to add manager:")
    print("Enter 4. to see the details:")
    print("Enter 0. to exit:\n")

    choice = int(input("Enter your choice:\n"))

    if choice==1:
        id=int(input("enter person id : "))
        name=input("enter person name :")
        age=int(input("enter person age :"))
        salary=int(input("enter personn salary :"))
        ps=Persons(id,name,age,salary)
        Persons.append(ps)

        print("you create a person !")

    elif choice==2:
        id=int(input("enter employee id : "))
        name=input("enter employee name :")
        age=int(input("enter employee age :"))
        salary=int(input("enter employee salary :"))
        hr=input("enter employee hr :")
        finance=input("enter employee finance :")

        es=employee(id,name,age,salary,hr,finance)
        employee.append(es)

    elif choice==3:
        id=int(input("enter manager id : "))
        name=input("enter manager name :")
        age=int(input("enter manager age :"))
        salary=int(input("enter manager salary :"))
        language=input("enter manager language :")

        ms=manager(id,name,age,salary,language)
        manager.append(ms)

    elif choice==4:
        print("Choose details to show:\n")

        print("Enter 1. for person details:")
        print("Enter 2. for employee details:")
        print("Enter 3. for manager details:")
        print("Enter 3. for live:")

        ch = int(input("Enter your choice: "))

        if ch==1:
            for ps in Persons:
                Persons.getdata()

        elif ch==3:
            for ma in manager:
                manager.getdata()

        elif ch==2:
            for es in employee:
                employee.getdata()

        elif ch==0:
            break

        else:
            print("you enter right number !")

    elif choice==0:
        print("thank you !")
        break

    else:
        print("you enter right number")                

    
