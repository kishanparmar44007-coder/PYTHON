
import numpy as np

print("\nWelcome to the numpy Analyzer !")
print("===============================\n")

def created_a_array_():
    print("\nSelect the type of array to create:")
    print("1. 1D Array")
    print("2. 2D Array")
    print("3. 3D Array")     

    try:
        choice = int(input("Enter your choice: "))
    except:
        print("Invalid input!")
        return None

    if choice == 1:
        size = int(input("Enter number of elements: "))
        elements = list(map(int, input("Enter elements separated by space: ").split()))

        if len(elements) != size:
            print("Error: Element count mismatch!")
            return None

        arr = np.array(elements)
        print("\n1D Array created successfully!")
        print(arr)
        return arr

    elif choice == 2:
        rows = int(input("Enter rows: "))
        cols = int(input("Enter columns: "))

        total = rows * cols
        print("\nEnter elements row-wise separated by space:")
        elements = list(map(int, input().split()))

        if len(elements) != total:
            print("Error: Element count mismatch!")
            return None

        arr = np.array(elements).reshape(rows, cols)
        print("\n2D Array created successfully!")
        print(arr)
        return arr

    elif choice == 3:
        depth = int(input("Enter depth (number of matrices): "))
        rows = int(input("Enter rows: "))
        cols = int(input("Enter columns: "))

        total = depth * rows * cols
        print(f"\nEnter {total} elements separated by space:")
        elements = list(map(int, input().split()))

        if len(elements) != total:
            print("Error: Element count mismatch!")
            return None

        arr = np.array(elements).reshape(depth, rows, cols)
        print("\n3D Array created successfully!")
        print(arr)
        return arr

    else:
        print("Invalid choice!")
        return None




def math_operatr(arr):
    print("\nMathematical operations:")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("============================================\n")

    choice = int(input("Enter your choice: "))
    n = int(input("Enter number: "))
    print("============================================\n")

    if choice == 1:
        print(arr + n)
    elif choice == 2:
        print(arr - n)
    elif choice == 3:
        print(arr * n)
    elif choice == 4:
        if n == 0:
            print("Error: Cannot divide by zero!")
        else:
            print(arr / n)
    else:
        print("Invalid choice!")




def searchsort_a_filter(arr):
    print("\nSearch, Sort and Filter:")
    print("1. Search element")
    print("2. Sort array")
    print("3. Filter array")
    print("============================================\n")

    choice = int(input("Enter  your choice: "))
    print("============================================\n")

    if choice == 1:
        x = int(input("Enter element to search: "))
        positions = np.where(arr == x)
        print("Positions:", positions)

    elif choice == 2:
        print("Sorted array:", np.sort(arr, axis=None))

    elif choice == 3:
        limit = int(input("Show elements greater than: "))
        print(arr[arr > limit])

    else:
        print("Invalid choice!")




def aggregation(arr):
    print("\nChoose aggregation/statistical operation:")
    print("1. Sum")
    print("2. Mean")
    print("3. Median")
    print("4. Max")
    print("5. Min")
    print("============================================\n")

    choice = int(input("Enter your choice: "))
    print("============================================\n")

    if choice == 1:
        print("Sum =", np.sum(arr))
    elif choice == 2:
        print("Mean =", np.mean(arr))
    elif choice == 3:
        print("Median =", np.median(arr))
    elif choice == 4:
        print("Max =", np.max(arr))
    elif choice == 5:
        print("Min =", np.min(arr))
    else:
        print("Invalid choice!")

def combined_arrays(arr):
    print("\nCombine arrays:")
    print("1. Horizontal")
    print("2. Vertical")
    print("============================================\n")

    choice = int(input("Enter your choice: "))
    print("============================================\n")

    print("Enter elements for another array:")
    new = list(map(int, input("Enter elements: ").split()))
    arr2 = np.array(new)

    try:
        if choice == 1:
            print("Combined (Horizontal):")
            print(np.hstack((arr, arr2)))

        elif choice == 2:
            print("Combined (Vertical):")
            print(np.vstack((arr, arr2)))

        else:
            print("Invalid choice!")

    except:
        print("Shape mismatch! Cannot combine arrays.")



def split_array(arr):
    print("\nSplit array:")
    print("1. Horizontal split")
    print("2. Vertical split")
    print("============================================\n")

    choice = int(input("Enter your choice: "))
    print("============================================\n")

    try:
        if choice == 1:
            print(np.hsplit(arr, 2))

        elif choice == 2:
            print(np.vsplit(arr, 2))

        else:
            print("Invalid choice!")

    except:
        print("Error: Array cannot be split evenly!")


def main():
    arr = None

    while True:
        print("\nChoose an option:")
        print("1. Create array")
        print("2. Mathematical operations")
        print("3. Search, sort, filter")
        print("4. Aggregation / Statistics")
        print("5. Combine arrays")
        print("6. Split arrays")
        print("7. Exit")
        print("============================================")
        choice = int(input("\nEnter your choice: "))
        print("============================================")

        if choice == 1:
            arr = created_a_array_()

        elif choice == 2 and arr is not None:
            math_operatr(arr)

        elif choice == 3 and arr is not None:
            searchsort_a_filter(arr)

        elif choice == 4 and arr is not None:
            aggregation(arr)

        elif choice == 5 and arr is not None:
            combined_arrays(arr)

        elif choice == 6 and arr is not None:
            split_array(arr)

        elif choice == 7:
            print("Thank you for using the Numpy Multitool!")
            break

        else:
            print("Please create an array first!")


main()
