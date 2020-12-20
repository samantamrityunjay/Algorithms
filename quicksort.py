initial_input = []

n = int(input("Enter number of integers: "))
for _ in range(n):
    initial_input.append(float(input()))
print("Initial List: ", initial_input)

def quicksort(sequence):
    length=len(sequence)
    if length<=1:
        return sequence
    else:
        pivot=sequence.pop()
    return quicksort([i for i in sequence if i<pivot])+[pivot]+quicksort([i for i in sequence if i>=pivot])

print("sortedlist: ",quicksort(initial_input))
        
        
    

