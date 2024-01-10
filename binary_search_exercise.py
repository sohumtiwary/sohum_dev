'''
Binary Search
'''

def main():
    test = [1, 2, 3, 6, 8, 19, 20]
    x = 19

    print("The value", x, "is at index", binary_search(test, x))


def binary_search(test, x):
    highIndex = len(test) - 1
    lowIndex = 0
    

    while lowIndex <= highIndex:
        midIndex = (highIndex + lowIndex) // 2

        if test[midIndex] < x:
            lowIndex = midIndex + 1
        
        elif test[midIndex] > x:
            highIndex = midIndex - 1

        else:
            return midIndex
    
    return -1

main()
