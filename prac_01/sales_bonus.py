"""
Program to calculate and display a user's bonus based on sales.
If sales are under $1,000, the user gets a 10% bonus.
If sales are $1,000 or over, the bonus is 15%.
"""
BONUS_L = 0.1
BONUS_H = 0.15
sales = float(input("Enter Sales:$ "))


while sales > 0:

    if sales < 1000:
        bonus = sales * BONUS_L
    else:
        bonus = sales * BONUS_H

    print(f"Your bonus is ${bonus:.2f}")
    sales = float(input("Enter Sales:$ "))

print("Invalid number")

