# Initialize a List:
lst1 = ["sana", 3, "car", 123, "sir"]

# Accessing Elements:
def access(lst1, index):
    if index < 0 or index >= len(lst1):  # Fixed: should be >= not >
        return "Index out of range"
    return lst1[index]

# Modifying Elements:
def modify(lst1, index, new):
    if index < 0 or index >= len(lst1):  # Fixed: check before modifying
        return "Index out of range"
    lst1[index] = new
    return f"Element modified. Updated list: {lst1}"

# Slicing the List:
def slice_list(lst1, start_index, end_index):
    if start_index < 0 or end_index > len(lst1) or start_index > end_index:
        return "Invalid indices"
    return lst1[start_index:end_index]

# Game Interaction:
def main():
    print("Welcome to the Indexing Game!")
    while True:
        print("\nSelect an operation:")
        print("1. Access an element (access)")
        print("2. Modify an element (modify)")
        print("3. Slice the list (slice)")
        print("4. Exit")
        operation = input("Enter the operation (access/modify/slice/exit): ").lower()

        if operation == "access":
            try:
                idx = int(input("Enter the index to access: "))
                print(access(lst1, idx))
            except ValueError:        #You give a value of the wrong type 
                print("Please enter a valid number!")

        elif operation == "modify":
            try:
                idx = int(input("Enter the index to modify: "))
                new_value = input("Enter the new value: ")
                print(modify(lst1, idx, new_value))
            except ValueError:
                print("Please enter a valid number!")

        elif operation == "slice":
            try:
                start = int(input("Enter the start index: "))
                end = int(input("Enter the end index: "))
                print(f"Sliced list: {slice_list(lst1, start, end)}")
            except ValueError:
                print("Please enter valid numbers!")

        elif operation == "exit":
            print("Thanks for playing the Indexing Game. Goodbye!")
            break
        else:
            print("Invalid choice. Please select access, modify, slice, or exit.")

if __name__ == "__main__":
    main()
