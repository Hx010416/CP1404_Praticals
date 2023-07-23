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

def main():
    user_input = input("Enter score: ")
    if user_input == "random":
        random_score = random.randint(0, 100)
        random_result = calculate_result(random_score)
        print(f"Random score: {random_score}, result: {random_result}")
    else:
        user_score = float(user_input)
        user_result = calculate_result(user_score)
        print(user_result)

if __name__ == '__main__':
    main()