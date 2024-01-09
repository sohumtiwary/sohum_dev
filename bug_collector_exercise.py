'''
Bug Collector Exercise
Bug collector collects bugs every day for five days.
Prgram keeps a running total of bugs collected in the five days.

-Ask amount of bugs collected every day for five days
-After loop is finished display amount of bugs collected
'''

total_bugs = 0
day = 0

while day < 5:
    input_bugs = float(input("How many bugs did you collect today? "))
    total_bugs += input_bugs
    day+=1

print("The total amount of bugs you collected over the five days was: ", total_bugs, " bugs")
