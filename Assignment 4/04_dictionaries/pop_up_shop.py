'''Write a program that loops through a dictionary of fruits, 
prompting the user to see how many of each fruit they want to buy, 
and then prints out the total combined cost of all of the fruits.

'''


fruits = {"cherry": 2.5,"melon": 5.0,"dragonfruit": 3.0,"kiwi": 4.0,"grape": 6.0,"mango": 3.5}
totalCost=0
for fruit,price in fruits.items():
    quantity=int(input(f"How many {fruit} do you want?:"))
    totalCost+=quantity*price
print(f"Your total is {totalCost:.2f}")
