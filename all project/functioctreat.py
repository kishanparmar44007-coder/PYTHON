def multi():
    minv = min(arry)
    maxv = max(arry)
    suum = sum(arry)
    l = len(arry)
    avg = sum(arry) / l if l > 0 else 0
    return {"minv": minv, "maxv": maxv, "sum": suum, "avg": avg}

def keys(*args):
    d = input("Enter data for 1D array (separated by spaces): ")
    db = d.split()
    for r in db:
        arry.append(int(r))
    return args

arry = []

while True:
    print("Welcome to the Data Analyzer and Transformer Program")
    print("Main menu:")
    print("1. Input Data")
    print("2. Display Data summary")
    print("3. Calculate Factorial")
    print("4. Filter data by threshold")
    print("5. Sort data")
    print("6. Display dataset statistics")
    print("7. Exit program")

    choice = int(input("Please enter your choice: "))

    if choice == 1:
        keys()
        print("\nData has been stored successfully!")

    elif choice == 2:
        if len(arry) == 0:
            print("No data found! Please input data first.")
        else:
            print("Data Summary:")
            print("- Total elements:", len(arry))
            print("- Minimum value:", min(arry))
            print("- Maximum value:", max(arry))
            print("- Sum of the values:", sum(arry))
            print("- Average value:", sum(arry) / len(arry))

    elif choice == 3:
        def factorial(num):
            if num <= 1:
                return 1
            else:
                return num * factorial(num - 1)

        num = int(input("Enter the number: "))
        result = factorial(num)
        print(f"The factorial of {num} is {result}")

    elif choice == 4:
        if len(arry) == 0:
            print("No data found! Please input data first.")
        else:
            threshold = int(input("Enter threshold value: "))
            filtered = [i for i in arry if i > threshold]
            print("Filtered data:", filtered)

    elif choice == 5:
        if len(arry) == 0:
            print("No data found! Please input data first.")
        else:
            print("Choose sorting option:")
            print("1. Ascending")
            print("2. Descending")

            sort_choice = int(input("Enter your choice: "))
            if sort_choice == 1:
                arry.sort()
                print("Sorted data (ascending):", arry)
            elif sort_choice == 2:
                arry.sort(reverse=True)
                print("Sorted data (descending):", arry)
            else:
                print("Invalid sorting choice.")

    elif choice == 6:
        if len(arry) == 0:
            print("No data found! Please input data first.")
        else:
            stats = multi()
            print("Dataset Statistics:")
            print("- Minimum value:", stats["minv"])
            print("- Maximum value:", stats["maxv"])
            print("- Sum:", stats["sum"])
            print("- Average:", stats["avg"])

    elif choice == 7:
        print("Exiting program.")
        break

    else:
        print("your choice is not her!")