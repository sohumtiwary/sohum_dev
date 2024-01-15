word1 = "abc"
word2 = "pqr"

output = []
string1 = [i for i in word1]
string2 = [i for i in word2]
i = 0
while i < len(word1) or i < len(word2):
    if i % 2 == 0:
        output.append(string1[i])
    else:
        output.append(string2[i])

    i += 1

print(output)