user_name = input("Enter your name: ")

# Task 1 - Writing user's name to a file in w mode
with open("name.txt", 'w') as file:
    file.writelines(user_name)

# Closing the file after writing is done
file.close()

# Task 2 - Reading the name from "name.txt" and printing it
with open("name.txt", 'r') as file:
    user_name = file.read().strip()

print(f"Your name is {user_name}")

# Closing the file after reading is done
file.close()

# Task 3 - Adding the first two numbers from "numbers.txt"
with open("numbers.txt", 'r') as file:
    numbers = file.readlines()

# Read the first line and convert it to an integer
number1 = int(numbers[0])
# Read the first line and convert it to an integer
number2 = int(numbers[1])
# Calculate the sum of the first two numbers
result = number1 + number2
print(f"The sum of the first two numbers is: {result}")

# Task 4 - Calculating the total of all numbers in a file
total = 0

with open("numbers.txt", 'r') as file:
    for line in file:
        # Convert each line to an integer and add it to the total
        total += int(line)

print(f"The total of all numbers in the file is: {total}")
