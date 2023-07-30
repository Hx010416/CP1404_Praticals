import random

print(random.randint(5, 20))  # line 1
print(random.randrange(3, 10, 2))  # line 2
print(random.uniform(2.5, 5.5))  # line 3
# On line 1, you will see a random integer between 5 and 20 (inclusive).
#
# The smallest number you could have seen is 5.
# The largest number you could have seen is 20.
#
# On line 2, you will see a random odd number between 3 and 9 (inclusive).
#
# The smallest number you could have seen is 3.
# The largest number you could have seen is 9.
# Line 2 could not have produced a 4 since the step is 2 (i.e., it skips even numbers).
#
# On line 3, you will see a random floating-point number between 2.5 and 5.5 (inclusive).
#
# The smallest number you could have seen is 2.5.
# The largest number you could have seen is 5.5.
import random

random_number = random.randint(1, 100)
print(random_number)
