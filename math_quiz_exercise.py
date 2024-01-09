import random

def main():
    x = random.randint(1,1000)
    y = random.randint(1,1000)
    
    print("What is the sum of", x, "and", y ,"?")
    answer = float(input("What is your answer?: "))
    correction(x, y, answer)


def correction(x, y, answer):
    while answer != x + y:
        print("You got the answer wrong. Try again.")
        answer = float(input("What is your answer?: "))
        if answer == x + y:
            print("Congrats! You got the answer right :)")

main()