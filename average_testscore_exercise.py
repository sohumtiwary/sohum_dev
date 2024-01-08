'''
TEST SCORE AVERAGE
Write a program that displays the average of three test scores

1) Get the first test score
2) Get the second test score
3) Get the third test score
4) Calculate the average
5) Display the average
'''

first_test = float(input("What is the score of your first test? "))
second_test = float(input("What is the score of your second test? "))
third_test = float(input("What is the score of your third test? "))

average_score = (first_test + second_test + third_test) / 3.0

print("The average of your three tests is:", average_score)