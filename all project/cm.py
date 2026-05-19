import time
import random
import uuid
import math
from datetime import datetime

def datetime_():
    while True:
        print("\nDatetime and Time Operations:")
        print("enter 1 to. Display current date and time")
        print("enter 2 to. Countdown Timer")
        print("enter 3 to exit :")
        

        choice = input("Enter your choice: ")

        if choice == "1":
            now = datetime.now()
            print("Current Date & Time:", now.strftime("%Y-%m-%d %H:%M:%S"))

        elif choice == "2":
            seco = int(input("Enter seconds: "))
            while seco > 0:
                print(seco)
                time.sleep(1)
                seco -= 1
            print("Time's Up!")

        elif choice == "3":
            break
        else:
            print("Invalid choice!")


def math_():
    while True:
        print("\nMathematical Operations:")
        print("enter 1 to. Factorial")
        print("enter 2 to. Compound Interest")
        print("enter 3 to exit :")

        choice = input("Enter your choice: ")

        if choice == "1":
            n = int(input("Enter number: "))
            print("Factorial:", math.factorial(n))

        elif choice == "2":
            pweee = float(input("Principal: "))
            reng = float(input("Rate (%): "))
            times = float(input("Time (years): "))
            ci = pweee * (1 + reng/100)**times
            print("Compound Interest:", round(ci, 2))

        elif choice == "3":
            break
        else:
            print("Invalid choice!")


def random_():
    while True:
        print("\nRandom Data Generation:")
        print("enter 1 to. Random Number")
        print("enter 2 to. Random Password")
        print("enter 3 to exit :")
        

        choice = input("Enter your choice: ")

        if choice == "1":
            print("Random Number:", random.randint(1, 100))

        elif choice == "2":
            lent = int(input("Password length: "))
            char = "89298252298hguyrrttyyr5etyftr"
            pwdew = "".join(random.choice(char) for _ in range(lent))
            print("Generated Password:", pwdew)

        elif choice == "3":
            break   
        else:
            print("Invalid choice!")


def uuid_():
    print("Generated UUID:", uuid.uuid4())


def file_():
    while True:
        print("\nFile Operations:")
        print("1. Create File")
        print("2. Write File")
        print("3. Read File")
        print("4. Append File")
        print("5. Back to Main Menu")

        choice = input("Enter your choice: ")

        if choice == "1":
            name = input("Filename: ")
            open(name, "w").close()
            print("File created.")

        elif choice == "2":
            name = input("Filename: ")
            text = input("Enter text: ")
            with open(name, "w") as f:
                f.write(text)
            print("Written.")

        elif choice == "3":
            name = input("Filename: ")
            with open(name, "r") as f:
                print("\nFile Content:\n", f.read())

        elif choice == "4":
            name = input("Filename: ")
            text = input("Enter text: ")
            with open(name, "a") as f:
                f.write("\n" + text)
            print("Added.")

        elif choice == "5":
            break
        else:
            print("Invalid choice!")


def explore():
    name = input("Enter module name: ")
    try:
        module = __import__(name)
        print(dir(module))
    except:
        print("Module not found!")


def main():
    while True:
        print("\n===============================")
        print("Welcome to Multi-Utility ! ")
        print("===============================")
        print("\n1. Datetime and Time Operations")
        print("2. Mathematical Operations")
        print("3. Random Data Generation")
        print("4. Generate UUID")
        print("5. File Operations")
        print("6. Explore Module (dir())")
        print("7. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            datetime_()
        elif choice == "2":
            math_()
        elif choice == "3":
            random_()
        elif choice == "4":
            uuid_()
        elif choice == "5":
            file_()
        elif choice == "6":
            explore()
        elif choice == "7":
            print("Thank you for using the Toolkit!")
            break
        else:
            print("Invalid choice!")

            if __name__ == "__main__":
                main()