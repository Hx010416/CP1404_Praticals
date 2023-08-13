COLORS = {"RED": "#FF0000",
          "ORANGE": "#FFA500",
          "YELLOW": "#FFFF00",
          "GREEN": "#008000",
          "BLUE": "#0000FF",
          "PURPLE": "#800080",
          "WHITE": "#FFFFFF",
          "BLACK": "#000000"}
while True:
    color_name = input("Enter a color name: ")
    if color_name == "":
        break
    color_hex = COLORS.get(color_name.upper())
    if color_hex is None:
        print("Invalid color name")
    else:
        print("{} is {}".format(color_name, color_hex))