t=[]

def create():
    number=int(input("enter the number of the list:"))
    for i in range(number):
            te=int(input(f" enter the number{i+1}:"))
            t.append(number)
    print("\nList created!\n")

def fact(num):
     if num<=1:
            return 1
     return num * fact(num-1)

while True:

    print("enter 1 to create a list")
    print("enter 2 to sum of the list")
    print("enter 3 to find max in the list")
    print("enter 4 to find min in the list")
    print("enter 5 to find average of the  list")
    print("enter 6 to find fact of the list")
    print("enter 0 to exit\n")

    chioce=int(input("enter your choice:"))

    
    if chioce == 1:
          create()
    elif chioce==2:
          print(sum(t))

    elif chioce==3:
          number=int(input("enter the number for find mix number"))
          print(max(number))

    elif chioce==4:
          number=int(input("enter the number for find min number"))
          print(min(number))

    elif chioce==5:
          print(sum(t)/len(t))

    elif chioce==6:
          num = int(input("enter the number for find fact number"))
          result = fact(num)
          print()

    elif chioce==0:
          print("thank you!")
          break

    else:
          print("your choice is not her!")