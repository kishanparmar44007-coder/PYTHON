students=[]

while True:

    print("welcome to the students list !")

    print("1. for add student ")
    print("2. for updet student")
    print("3. for delet student")
    print("4. for read student")
    print("0. for exit")

    choice=int(input("enter your choice :"))

    if choice==1:
        st={
            "id" :int(input("enter the student id : ")),
            "name" :input("enter the student name : "),
            "age" :int(input("enter the student age : ")),
            "city":input("enter oyur city :")
        }

        students.append(st)

    elif choice==2:
        id=int(input("enter student id for updet :"))
        for st in students:
            if st ["id"] == id:
                st["name"]==(input("enter new name:"))
                "age"==int(input("enter new age:"))
                "city"==(input("enter new city:"))

    elif choice==3:
        id=int(input("enter student id for remove :"))
        for st in students:
            if st ["id"] == id:
                students.remove(st)
                
    elif choice==4:
        for st in students:
            print(f"stundent name : {st["name"]}")

            print(tuple())