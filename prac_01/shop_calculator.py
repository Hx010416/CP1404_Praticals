num_items = -1
while num_items < 0:
    num_items_str = input("Number of items: ")
    if num_items_str. isdigit():
        num_items = int(num_items_str)
        if num_items < 0:
            print("Invalid number of items!")
    else:
        print("Invalid input! Please enter a whole number.")

total_price = 0

for i in range(num_items):
    valid_price = False
    while not valid_price:
        price_str = input("Price of item:$ ")
        if price_str.replace(".", "", 1). isdigit():
            price = float(price_str)
            if price >= 0:
                valid_price = True
            else:
                print("Invalid price!")
        else:
            print("Invalid input! Please enter a number.")
    total_price += price

if total_price > 100:
    total_price *= 0.9

print("Total price for %d items is $%.2f" % (num_items, total_price))
