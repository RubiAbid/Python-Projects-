'''Write a function that takes a list of numbers and returns the sum of those numbers.'''

def lists(numbers):
    total = sum(numbers)  
    return total

if __name__ == "__main__":
    result = lists([2, 3, 4, 5, 6])
    print(f"The sum is: {result}")
