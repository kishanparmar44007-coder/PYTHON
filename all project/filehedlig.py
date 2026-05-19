class custom(Exception):
    pass

class hendling:
    def __init__(self, file_name="mord.txt"):
        self.file_name = file_name

    def new_entry(self):
        try:
            with open(self.file_name, "a") as file:
                id = int(input("enter your id:\n"))
                new_entry_input = input("enter your journal entry !\n")
                file.write(f"{id}: {new_entry_input}\n")
                print("the entry added successfully!")
        except FileNotFoundError:
            print("FileNotFoundError please make file!")
        except Exception :
            print(f"An error occurred: ")

    def view_entry(self):
        try:
            with open(self.file_name, "r") as file:
                import datetime
                now = datetime.datetime.now()
                print("Current Date & Time:", now)
                print("-----------------------------------------------------\n")
                for line in file:
                    print(line)
        except FileNotFoundError:
            print("File not found!")

    def search_entry(self):
        try:
            with open(self.file_name, "r") as file:
                id = int(input("enter your id:\n"))
                found = False
                for line in file:
                    if str(id) in line:
                        print(line)
                        found = True
                if not found:
                    print("you entered id is not found!")
        except FileNotFoundError:
            print("File not found!")

    def delete_entry(self):
        try:
            print("your all entry is delete (yes/no):")
            print("enter 1 to yes:")
            print("enter 2 to no:")
            choice = input("enter your choice:")
            if choice == "1":
                id = int(input("enter your id:\n"))
                with open(self.file_name, "r") as file:
                    lines = file.readlines()
                with open(self.file_name, "w") as file:
                    for line in lines:
                        if str(id) not in line:
                            file.write(line)
                        else:
                            print("entry deleted")
            else:
                print("thank you!")
        except FileNotFoundError:
            print("File not found!")

file_manager = hendling()

while True:
    print("welcome to personal journal manager!")
    print("please select an option:")
    print("1. add a new entry")
    print("2. view all entries")
    print("3. search for an entry")
    print("4. delete entries")
    print("0. exit the program")

    try:
        choice = int(input("enter your choice: \n"))
    except ValueError:
        print("Invalid input! Please enter a number.")
        continue

    if choice < 0 or choice > 4:
        print("the number is not in choice")
        continue

    if choice == 1:
        file_manager.new_entry()
    elif choice == 2:
        file_manager.view_entry()
    elif choice == 3:
        file_manager.search_entry()
    elif choice == 4:
        file_manager.delete_entry()
    elif choice == 0:
        print("thank you! good bye!")
        break
