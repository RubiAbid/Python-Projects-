'''This program counts the number of times each number appears in a list. It uses a dictionary to keep track of the information.

'''

def main():
    lst = []  # Store all the numbers 
    while True:
        lst1 = input("Enter a number (or press Enter to finish): ")
        if lst1 == "":
            break
        num = int(lst1)
        lst.append(num)

    # Count how many times each number appears
    count_dict = {}
    for i in lst:
        if i in count_dict:    # check , Does this number already exist as a key in the dictionary count_dict
            count_dict[i] += 1
        else:
            count_dict[i] = 1

    print("\nNumber frequencies:")
    for k, v in count_dict.items():
        print(f"{k} appears {v} times")

if __name__ == '__main__':
    main()
