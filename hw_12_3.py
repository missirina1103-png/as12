numbers = list(map(int, input().split()))
n=0
for i in range(len(numbers)):
    for k in range(i + 1, len(numbers)):
        if numbers[i] > numbers[k]:
            numbers[i], numbers[k] = numbers[k], numbers[i]
        n+=1

print("sorted list", numbers, "\n", "number of comparisons", n)