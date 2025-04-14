#Write a function that takes two numbers and finds the average between the two.



def average(num1: float, num2: float) -> float:
    averages = (num1 + num2) / 2
    return averages

def main():
   
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))
    
    result = average(num1, num2)
    print(f"The average of {num1} and {num2} is: {result}")

if __name__ == "__main__":
    main()
