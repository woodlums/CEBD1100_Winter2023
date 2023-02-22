import random

c = [[80, 72], [66, 77]]

print(c[1][1])

a = [1, 2]
b = [1, 2]

print(a == b)


squares = [value**2 for value in range(1, 11)]

print(squares)

random_ints = []
for n in range(100):
    random_ints.append(random.randint(1, 1000))

random_ints2 = [random.randint(1, 1000) for x in range(100)]

print(random_ints2)


thistuple = (1, 3, 7, 8, 7, 5, 4, 6, 8, 5)
x = thistuple.index(8)
print(x)
