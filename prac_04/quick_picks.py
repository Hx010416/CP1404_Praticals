import random

MIN_NUMBER = 1
MAX_NUMBER = 45
NUMBERS_PER_QUICK_PICK = 6
NUM_QUICK_PICKS = int(input("How many quick picks? "))

def generate_quick_pick():
    return sorted(random.sample(range(MIN_NUMBER, MAX_NUMBER + 1), NUMBERS_PER_QUICK_PICK))

def display_quick_picks():
    for _ in range(NUM_QUICK_PICKS):
        quick_pick = generate_quick_pick()
        print(" ".join(str(number).rjust(2) for number in quick_pick))

display_quick_picks()
