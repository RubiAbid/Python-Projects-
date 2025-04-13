'''Print 10 random numbers in the range 1 to 100.'''


import random

def randomNum():

   
    for i in range(10):
        number=random.randint(1,100)
        print(number)

if __name__=="__main__":
    randomNum()