while True:
    print("Wlcome to the patter Generator and Number Analyzer!")

    print()

    print("1. generate a Pattern")
    print("2. Analyze a Range of Number")
    print("3. Exit")

    choice=int(input("Enter your choice:"))

    if choice==1:
        a=int(input("Enter the number of fows for the pattern:"))
        print()

        print("Pattern:")

        for i in range(1,a+1):
            print("* "*i)

    elif choice==2:
        start=int(input("Enter the start of the range :"))
        end=int(input("Enter the end of the range :"))
        all=0
       
        for T in range(start,end+1):
            if T %2==0:
                print("number",T,"is Even")

            else:
                print("number",T,"is Odd")
            all+=T

    
        print("Sum of all number from",start, "to",end,"is:",all,)
 
        print()

    elif choice==3:
        print("Exiting the program. Godbye!")

    else:
        print("your choice is not her!")
