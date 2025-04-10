'''Ask the user for a number and print its square (the product of the number times itself).

'''



def main():

 square=float(input("Enter a number to find its square : "))
 print(f"{square} squared is {square**2}")

if __name__=="__main__":
    main()