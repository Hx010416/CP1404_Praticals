
for i in range(1, 21, 2):
    print(i, end=' ')
print()

for i in range(0, 110, 10):
    print(i, end=' ')
print()

for i in range(20, 0, -1):
    print(i, end=' ')
print()

num_stars = int(input("Enter the number of stars:"));
for i in range(0, num_stars):
    print("*", end=' ')
print()

num_rows = int(input("Enter the number of rows:"));
k = 1
for i in range(0, num_rows):
    for j in range(0, k):
        print("* ", end='')
    k = k + 1
    print()

