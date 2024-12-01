with open("input.txt", "r") as f:
    fileInput = f.read().splitlines()
    total = [int(j) for i in fileInput for j in i.split() if j]

list1 = total[::2]
list2 = total[1::2]

list1.sort()
list2.sort()

# part 1
numSum = 0
for num1, num2 in zip(list1, list2):
    numSum += abs(num1 - num2)

# part 2
similarityScore = 0
for i in list1:
    similarityScore += i * list2.count(i)

print(numSum, similarityScore)