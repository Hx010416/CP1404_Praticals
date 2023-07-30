"""
CP1404/CP5632 - Practical
Answer the following questions:
1. When will a ValueError occur?
A ValueError will occur if the user enters a non-integer value for either the numerator or the denominator.
2. When will a ZeroDivisionError occur?
A ZeroDivisionError will occur if the user enters 0 as the denominator, which would result in a division by zero.
3. Could you change the code to avoid the possibility of a ZeroDivisionError?
Yes, ZeroDivisionError can avoid by adding a condition to check if the denominator is equal to 0 before performing the division.
"""

try:
    numerator = int(input("Enter the numerator: "))
    denominator = int(input("Enter the denominator: "))
    fraction = numerator / denominator
    print(fraction)
except ValueError:
    print("Numerator and denominator must be valid numbers!")
except ZeroDivisionError:
    print("Cannot divide by zero!")
print("Finished.")