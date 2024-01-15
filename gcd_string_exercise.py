str1="ABCABC"
str2="ABC"
output = []

arr1 = [i for i in str1]
arr2 = [i for i in str2]

i = 0

while i < len(str1) and i < len(str2):
    if arr1[i] == arr2[i]:
        arr1[i] = 0
        arr2[i] = 0
    else:
        output.append(arr1[i])

    i += 1

print(''.join(output))