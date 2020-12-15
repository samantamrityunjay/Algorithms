
initial_input = []
sorted_output = []
n = int(input("Enter number of integers: "))
for _ in range(n):
    initial_input.append(float(input()))
sorted_output = initial_input[:]
print(initial_input)
while True:
    count = 0
    for i in range(n-1):
        if sorted_output[i] > sorted_output[i+1]:
            temp = sorted_output[i]
            sorted_output[i] = sorted_output[i+1]
            sorted_output[i+1] = temp
            count += 1
    if count == 0:
        break
print(sorted_output)
