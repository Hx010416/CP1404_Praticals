import random

def calculate_result(score):
    if score < 0 or score > 100:
        return "Invalid score"
    elif score >= 90:
        return "Excellent"
    elif score >= 50:
        return "Passable"
    else:
        return "Bad"

def get_valid_score():
    while True:
        try:
            score = float(input("Enter score (0-100): "))
            if score < 0 or score > 100:
                print("Invalid score, try again.")
            else:
                return score
        except ValueError:
            print("Invalid input, try again.")

def print_result():
    score = get_valid_score()
    result = calculate_result(score)
    print(f"Result: {result}")

def show_stars():
    score = get_valid_score()
    stars = "*" * int(score)
    print(f"Stars: {stars}")

def main():
    while True:
        print("\nMENU")
        print("(G)et a valid score")
        print("(P)rint result")
        print("(S)how stars")
        print("(Q)uit")
        choice = input("Enter your choice: ").lower()
        if choice == "g":
            get_valid_score()
        elif choice == "p":
            print_result()
        elif choice == "s":
            show_stars()
        elif choice == "q":
            print("Goodbye!")
            break
        else:
            print("Invalid choice, try again.")

if __name__ == '__main__':
    main()
