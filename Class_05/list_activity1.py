import random

# FUNCTION -> random.randint(1, 1000)

#1 - Create a list of 100 random number from 1 to 1000

random_ints = []

for n in range(100):
    random_ints.append(random.randint(1, 1000))

print(random_ints)

# Find min, max and sum
min_value = random_ints[0]
max_value = 0
total_sum = 0

for n in random_ints:
    # total_sum = total_sum + n
    total_sum += n

    if n > max_value:
        max_value = n

    if n < min_value:
        min_value = n

# Find the largest integer in this list. (The easy way and the hard way).
print("Using MAX function ->" + str(max(random_ints)))
print(max_value)


# Find the smallest integer in this list.
print(min(random_ints))
print(min_value)

# What is the average?

print("Average")
print(total_sum / len(random_ints))



# for x in range(100):
#     print(random_ints[x])

for x in random_ints:
    print(x)
