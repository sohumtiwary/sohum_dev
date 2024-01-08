'''
Convert Savings Account formula into code, wanna output how much money they should invest based off of F,r, and n
Formula: P = F / ((1+r)**n)

P = Present value
F = Future value you want in the account
r = annual interest rate 
n = number of years you plan to let the money sit in the account 

1. Ask for F
2. Ask for r
3. Ask for n
'''

future_value = float(input("How much money do you want in the account in the future? "))
rate = float(input("What is the annual interest rate right now? "))
amt_of_years = int(input("How many years can you keep this money in the account? "))

denominator = (1 + rate)**amt_of_years

present_value = future_value/denominator

print("You'll have to invest " + str(present_value) + " in your savings account right now.")