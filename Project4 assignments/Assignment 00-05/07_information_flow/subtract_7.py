'''Fill out the subtract_seven helper function to subtract 7 from num, and fill out the main() method to call the subtract_seven helper function! If you're stuck, revisit the add_five example from lecture.
'''


def subtract_seven(num):
   return num-7




def main():
    number = input("Enter a number: ")
    if number.isdigit():
        num=int(number)
        result=subtract_seven(num)
        print(f"{num} - 7 = {result}")
    else:
        print("Please enter a valid number.")

if __name__ == '__main__':
    main()