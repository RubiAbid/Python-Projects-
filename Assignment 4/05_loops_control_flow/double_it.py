'''
Write a program that asks a user to enter a number. Your program will then double that number and print out the result. It will repeat that process until the value is 100 or greater.

For example if the user enters the number 2 you would then print:

4 8 16 32 64 128'''




number=int(input("Enter a number:"))
while number<100:
    number*=2
    print(number)
