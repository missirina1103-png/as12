numbers = list(map(int, input().split()))

for i in range(len(numbers)):
    for k in range(i + 1, len(numbers)):
        if numbers[i] > numbers[k]:
            numbers[i], numbers[k] = numbers[k], numbers[i]

print(numbers)