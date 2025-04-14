'''Write a program which prompts the user for a temperature in Fahrenheit (this can be a number with decimal places!) and outputs the temperature converted to Celsius.'''

def main():

  degrees_fahrenheit =int(input("Enter temperature in fehreheit : "))
  degrees_celsius = (degrees_fahrenheit - 32) * 5.0/9.0
  print(f'Temperature in celcius is {degrees_celsius}C')



if __name__=='__main__':
    main()
