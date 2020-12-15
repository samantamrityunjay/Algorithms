initial_input = []

n = int(input("Enter number of integers: "))
for _ in range(n):
    initial_input.append(float(input()))
print("Initial List: ", initial_input)

for i in range(n-1):
    min = initial_input[i]
    for j in range(i, n):
        if min > initial_input[j]:
            min = initial_input[j]
            temp = initial_input[i]
            initial_input[i] = initial_input[j]
            initial_input[j] = temp
print("Sorted List: ", initial_input)
