'''Fill out the function count_even(lst) which

first populates a list by prompting the user for integers until they press enter (please use the prompt "Enter an integer or press enter to stop: "),

and then prints the number of even numbers in the list.

If you'd prefer to focus on the second task only, scroll down for our implementation of the first task!'''



def count_even(lst):
    even_count = 0
    for num in lst:
        if num % 2 == 0:
            even_count += 1
    print(f"Number of even integers: {even_count}")
    
def main():
    lst = []
    while True:
        numbers = input("Enter a number (or press enter to stop): ")
        if numbers == '':
            break
        if numbers.isdigit():
            num = int(numbers)
            lst.append(num)
        else:
            print("Enter a valid number")
    count_even(lst)

if __name__ == "__main__":
    main()




 
        