student=[]    

while True:
    print("welcome to the Student Data Organizer!")

    print("Select an option:")

    print("1. Add student")
    print("2. Dispiay all Student")
    print("3. updete student Information")
    print("4. Delet Student")
    print("5. Display subjects offered")
    print("6. Exit\n")

    choice=int(input("Enetr your choice:"))
    
    if choice==1:
        print("Enter your details:")
        st={
            "id" :tuple(input("Enter student id :"),),
            "name" :input("Name : "),
            "age" :int(input("Age: ")),
            "Grade":input("Grade:"),
            "dob" :tuple(input("date of Birth (YYYY-MM-DD): "),),
            "subjects":(input("subjects(comma-separated):"))
        }

        student.append(st)
        print("Student added successfully!")

    elif choice==2:
        id=input("enter student id:")
        for st in student:
            print(st)
            if st["id"][0]==id:
                print(f"student ID:{st["id"]}|Name:{st["name"]}|Age{st["age"]}|Graed:{st["Grade"]}|Subjects:{st["subjects"]}|")


    elif choice==3:
        id=(input("enter student id:"))
        for st in student:
            if st["id"][0]==id:
                st["name"]=input("Name : ")
                st["age"]=int(input("Age: "))
                st["Grade"]=input("Grade:")
                st["dob"]=(input("date of Birth (YYYY-MM-DD): "))
                st["subjects"]=input("subjects(comma-separated):")

            print("Student updet successfully!")

    elif choice==4:
        id=input("enter student id for remove :")
        for st in student:
            if st["id"][0]==id:
                del st
        print("Student delet successfully!")
    
    elif choice==5:
        id=(input("enter student id:"))
        for st in student:
            if st["id"][0]==id:
                print(f"Subjects:{st["subjects"]}")

    elif choice==6:
        print("THANK YOU!")
        break

    else:
        print("your choice is not her")