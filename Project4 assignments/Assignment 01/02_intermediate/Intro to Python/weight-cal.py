''' Write a Python program that prompts an Earthling to enter their weight on Earth and prints their calculated weight on Mars.

The output should be rounded to two decimal places when necessary. Python has a round function which can help you with this. You pass in the value to be rounded and the number of decimal places to use. In the example below, the number 3.1415926 is rounded to 2 decimal places which is 3.14.

'''

earth_weight_input = input("Enter your weight on Earth (kg): ")

# Convert input to float
earth_weight = float(earth_weight_input)


planet = input("Enter the name of a planet (e.g., Mars): ")

# Dictionary of planet gravity ratios
gravity_factors = {
    "mercury": 0.376,
    "venus": 0.889,
    "mars": 0.378,
    "jupiter": 2.36,
    "saturn": 1.081,
    "uranus": 0.815,
    "neptune": 1.14
}

# Calculate and print weight on the selected planet
if planet in gravity_factors:
    planet_weight = round(earth_weight * gravity_factors[planet], 2)
    print(f"Your weight on {planet} would be {planet_weight} kg.")
