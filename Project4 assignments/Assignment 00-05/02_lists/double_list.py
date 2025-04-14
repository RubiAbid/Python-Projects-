'''Write a program that doubles each element in a list of numbers. For example, if you start with this list:

numbers = [1, 2, 3, 4]

You should end with this list:

numbers = [2, 4, 6, 8]'''


def double(numbers):
    double=[x*2 for x in numbers ]
    return double

if __name__=="__main__":
    result=double([1,2,3,4])
    print(f"The double of given list is : {result}")
