def main():
    MIN_PASSWORD_LENGTH = 8
    password = get_password(MIN_PASSWORD_LENGTH)
    print_asterisks(password)

def get_password(min_length):
    while True:
        password = input("Please enter a password: ")
        if len(password) < min_length:
            print(f"Error: Password must be at least {min_length} characters long.")
        else:
            return password

def print_asterisks(password):
    print("*" * len(password))

if __name__ == '__main__':
    main()