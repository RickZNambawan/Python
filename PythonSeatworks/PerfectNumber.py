""" A positive integer is said to be a perfect number if it is equal to all its divisors, excluding itself.
    For example, 6 is a perfect number since 6 = 1 + 2 + 3. But 8 is not a perfect number since 8 != 1 + 2 + 4.

    Write a program that accepts a positive integer that is less than 10,000 and determines whether the
    integer is a perfect number or not.

    Sample:
    Enter a number: 6
    6 is a Perfect Number.

    Enter a number: 8
    8 is not a Perfect Number.

    Enter a number: -9
    Zero or negative number is not allowed.
"""

# Program: Perfect Number or Not
# Perfect Numbers that are less than 10,000 are: 6, 28, 496 and 8,128

number = int(input("Enter a number: "))
if number <= 0:
    print("Zero or negative number is not allowed.")
elif number > 10000:
    print("Number greater than 10,000 is not allowed.")
else:
    total = 0
    for num in range(1, number):
        if (number % num) == 0:
            total += num

    if total == number:
        print("{:,} is a Perfect Number.".format(number))
    else:
        print("{:,} is not a Perfect Number.".format(number))































