
'''
Converts feet to inches.
Feet is an American unit of measurement.
There are 12 inches per foot.
'''

def main():
    value_in_feet = float(input("Enter value to convert into inches: "))
    inches = value_in_feet * 12
    print(f"{value_in_feet} feet is equal to {inches} inches.")

if __name__ == '__main__':
    main()
