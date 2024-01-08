'''
Grading scale
'''

GRADE_A = 90
GRADE_B = 80
GRADE_C = 70
GRADE_D = 60
GRADE_F = 50

user_grade = float(input("What is your numeric grade? "))

if(user_grade >= GRADE_A and user_grade < 101):
    print("Congrats! You got an A.")
elif(user_grade >= GRADE_B and user_grade < 91):
    print("You got a B.")
elif(user_grade >= GRADE_C and user_grade < 81):
    print("You got a C.")
elif(user_grade >= GRADE_D and user_grade < 71):
    print("You got a D.")
elif(user_grade >= GRADE_F and user_grade < 61):
    print("You got an F.")
else:
    print("You put an invalid input")