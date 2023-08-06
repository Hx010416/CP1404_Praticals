def main():
    # Prompt the user for 5 numbers and store them in a list called 'numbers'
    numbers = []
    for i in range(5):
        number = float(input("Number: "))
        numbers.append(number)

    # Output information about the numbers
    print(f"The first number is {numbers[0]}")
    print(f"The last number is {numbers[-1]}")
    print(f"The smallest number is {min(numbers)}")
    print(f"The largest number is {max(numbers)}")
    print(f"The average of the numbers is {sum(numbers) / len(numbers):.1f}")

def security_checker():
    # List of authorized users
    usernames = ['jimbo', 'giltson98', 'derekf', 'WhatSup', 'NicolEye', 'swei45', 'BaseInterpreterInterface',
                 'BaseStdIn', 'Command', 'ExecState', 'InteractiveConsole', 'InterpreterInterface',
                 'StartServer', 'bob']

    # Ask the user for their username
    username = input("Please enter your username: ")

    # Check if the username is in the list of authorized users
    if username in usernames:
        print("Access granted")
    else:
        print("Access denied")


if __name__ == "__main__":
    main()
    security_checker()