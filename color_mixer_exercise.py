'''
Color Mixing Program

When you mix two primary colors, you get a secondary color
If user enters an input that aren't two primary colors than give an error message

Red and Blue -> Purple
Red and Yellow -> Orange
Blue and Yellow -> Green
'''

red = "red"
blue = "blue"
yellow = "yellow"

color1 = str(input("Enter a primary color: "))
color2 = str(input("Enter a second primary color: "))

if (color1 == red or color1 == blue or color1 == yellow) and (color2 == red or color2 == blue or color2 == yellow):
    if color1 == red and color2 == blue:
        print("You got purple!")
    elif color1 == red and color2 == yellow:
        print("You got orange!")
    elif color1 == blue and color2 == yellow:
        print("You got green!")
    else:
        print("You picked the same color twice!")
else:
    print("Error! You did not enter a primary color!")