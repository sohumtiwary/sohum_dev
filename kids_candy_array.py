candies = [2, 3, 5, 1, 3]
extraCandies = 3

output = []

max = max(candies)

for i in range(len(candies)):
    sum = candies[i] + extraCandies
    if sum >= max:
        output.append("true")
    else:
        output.append("false")

print(output)