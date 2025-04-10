'''Write a program that continually reads in mass from the user and then outputs the equivalent energy using Einstein's mass-energy equivalence formula (E stands for energy, m stands for mass, and C is the speed of light:

E = m * c**2

Almost 100 years ago, Albert Einstein famously discovered that mass and energy are interchangeable and are related by the above equation. You should ask the user for mass (m) in kilograms and use a constant value for the speed of light -- C = 299792458 m/s.

'''


def main():
    m=float(input("Enter value of mass :"))
    C= 299792458
    e:float=m*(C**2)
    print("formula : e= m*c^2")
    print(f"VAlue of C : {C}m/s")
    print(f"Value of mass : {m} kg")
    print(f"Einstein's mass-energy equivalence formula : {e} joules of energy")


if __name__=="__main__":
    main()