import datetime,time


def fact(num):
     if num<=1:
            return 1
     return num * fact(num-1)

while True:
    print("======================================================")
    print("welcome to muti-utility toolkit:")
    print("======================================================")

    print("chooes an option:")
    print("1. datatime and time operations")
    print("2. mathematical operations")
    print("3. random data genration ")
    print("4. generate uniqe identifiers(UUID)")
    print("5. file opterations(custom module)")
    print("0.exit")

    print("======================================================")
    choice=int(input("\nenter your choice :"))

    if choice==1:
        while True:
                print("datatime and time operations :")
                print("1. display current date and time :")
                print("2. calculater difference between two dates / time :")
                print("3. format date into custom format :")
                print("4. stopewatch :")
                print("5. contdown timer :")
                print("0. to retun main menu :")

                ch=int(input("\nenter your choice:"))

                if ch==1:
                
                    now=datetime.datetime.now()
                    fdate=now.strftime("%d-%m-%Y %H: %M: %S")
                    print("======================================================")                

                elif ch==2:
                    d1=int(input("enter frist date (YYYY-MM-DD):"))
                    d2=int(input("enter second date (YYYY-MM-DD):"))
                    print(d1-d2)

                    print("======================================================")
                            
                elif ch==5:
                    
                    tim=int(input("enter your contdown time :"))
                    time.sleep(tim)
                    for tim in range:
                         print(tim)
                    print("======================================================")
                elif ch==4:
                    tim=int(input("enter your contdown time :"))
                    time.sleep(1)
                    for i in range:
                         print(tim*i)
                    print("======================================================")

                elif ch==0:
                    print("thank you !")
                    print("======================================================")

                else:
                    print("your choice is not valide!")

    elif choice==2:
         while True:
              
            print("mathematical operations :")
            print("1. calculate factoriyal :")
            print("2. solue compound interest :")
            print("3. trigonomentric calcultations")
            print("4. area of geometric shapes")
            print("0. to retun main menu :")

            ch2=int(input("\nentre your choice :"))

            if ch2==1:
                 
                num = int(input("enter the number for find fact number"))
                result = fact(num)
                print("======================================================")

            elif ch2==2:
                amount=int(input("enter principal amount :"))
                interest=int(input("enter interest amount :"))
                timef=int(input("enter time (in year) amount :"))
                find=amount*(pow((1+interest/100),timef))
                last=find-amount
                print(f"compound interest :{last}")
                print("======================================================")
            
