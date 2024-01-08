'''
TIP TAX TOTAL
Program that calculates the total amount of a meal purchased at a restaurant.
Ask user to enter the charge for the food
Calculate the amounts of a 18 percent tip and 7 percent sales tax
'''

food_price = float(input("What is the price of the food? "))

tip = food_price * 0.18
tax = food_price * 0.07

total = food_price + tip + tax

print("The price of the meal was", format(food_price, '.2f'))
print("The tip was", format(tip, '.2f'))
print("The tax for the meal was", format(tax, '.2f'))
print("The total charge comes out to", format(total, '.2f'))