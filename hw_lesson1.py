# Homework for lesson 1 .30.07.2021
from math import pi


# ex. 1:
def calculate_sphere_volume(radius):
    """Takes a radius, calculates and returns V(volume) of sphere"""
    return 4 / 2 * pi * radius ** 3


print("exercise 1. Calculate V of sphere")
r = float(input("please input a radius: "))
print("The volume of a sphere of radius = ", r, "m is equal to: ", calculate_sphere_volume(r), "m**3", sep="")


# ex. 2
def simple_interest_formula(principal: int, interest: int, time_period: int, t=12):
    """Takes principal_amount, interest_rate, time, (optional: the accrual period. default = 12 month) and prints:
    The amount formed by the end of the term
    The interest for the entire term of the loan

    Principal(Р) - the initial amount of the deposit (loan)
    interest(i) - simple interest rate
    time_period(T) - loan term
    S - the amount formed by the end of the term
    interest(I) - interest for the entire term of the loan
    t - the accrual period
    n - the number of interest calculation
    """
    n = time_period // t
    S = principal * (1 + interest * n / 100)
    interest = principal * interest * n / 100
    print("The amount formed by the end of the term is: ", S)
    print("The interest for the entire term of the loan is :", interest)


print("\nexercise 2. Simple interest formula")
P = int(input("Input the initial amount of the deposit (loan): "))
i = int(input("Input the simple interest rate (%): "))
T = int(input("Input the loan term by month: "))
simple_interest_formula(P, i, T)


# ex. 3
def calculate_sphere_area(radius):
    """Takes a radius, calculates and returns A(area) of sphere"""
    return 4 * pi * radius ** 2


print("\nexercise 3. Area of Sphere")
r = float(input("please input a radius: "))
print("The area of a sphere of radius = ", r, "m is equal to: ", calculate_sphere_area(r), "m**2", sep="")


# ex. 4
def two_numbers_pow(num_1: int, num_2: int, power=2):
    """Takes two numbers and returns power of sum this numbers.(Pow is optional, default = 2)"""
    return (num_1 + num_2) ** power


print("\nexercise 4. (a+b)**2")
a = int(input("please input first number: "))
b = int(input("please input second number: "))
print("(", a, "+", b, ")**2 = ", two_numbers_pow(a, b))

# ex. 5
print("\nexercise 5. Assign value of a variable to b variable without using third variable")
a = int(input("please input first number: "))
b = int(input("please input second number: "))
print("before change: a =", a, "b =", b)
a, b = b, a  # Actually uses 2 extra temp variables in back :)
print("after change: a =", a, "b =", b)
