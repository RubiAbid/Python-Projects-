'''Write a program to print terms in the Fibonacci sequence up to a maximum value.
'''


MAX_value = 10000
first = 0
second = 1

print(first)  # Print initial value

while second < MAX_value:
    print(second)
    next = first + second
    first = second
    second = next


