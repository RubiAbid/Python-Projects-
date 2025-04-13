'''Write a program which asks a user for their age and lets them know if they can or can't vote in the following three fictional countries.
Around the world, different countries have different voting ages. In the fictional countries of Peturk'''



def main():
    age = int(input("Enter your age: "))
    
    if age >= 18:
        print("You are eligible to vote in Pakistan.")
    
    if age >= 16:
        print("You are eligible to vote in Brazil.")
    
    if age >= 15:
        print("You are eligible to vote in Iran.")
    
    else:
        print("You are not eligible to vote in any of the three countries.")

if __name__ == "__main__":
    main()

       
    
       


if __name__=="__main__":
    main()