# Read how many numbers will be entered
num_count = int(input())

# Initialize the counters and total
cou1 = 0      # Positive count
cou2 = 0      # Negative count
cou3 = 0      # Zero count
total = 0

# Read and analyze each number
for i in range(num_count):
    n = int(input())

    if n > 0:
        cou1 += 1
    elif n < 0:
        cou2 += 1
    else:
        cou3 += 1

    total += n

# Display the final analysis
print(f"Positive Count: {cou1}")
print(f"Negative Count: {cou2}")
print(f"Zero Count: {cou3}")
print(f"Total: {total}")