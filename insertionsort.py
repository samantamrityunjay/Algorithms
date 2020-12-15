initial_input = []
n = int(input("Enter number of integers: "))
for _ in range(n):
    initial_input.append(float(input()))

print("Initai list", initial_input)


def swapif_agreaterb(a, b):
    if a > b:
        temp = a
        a = b
        b = temp
        return a, b
    else:
        return False


for i in range(1, n):
    if initial_input[i-1] > initial_input[i]:
        for j in range(i):
            if swapif_agreaterb(initial_input[i-j-1], initial_input[i-j]):
                initial_input[i-j-1], initial_input[i-j] = swapif_agreaterb(
                    initial_input[i-j-1], initial_input[i-j])
            else:
                break

print("Sorted list", initial_input)
