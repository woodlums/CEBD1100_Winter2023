name = "Concordia" #string

name_list = list(name)

vowels = 0
for x in name_list:
    if x in "aeiou":
        vowels += 1

print(vowels)

a = (1, 2, 3)

print(type(a))

my_list1 = ["red", "blue", "green", "pink"]
my_list2 = [2, "hello", True]
my_list3 = [my_list1, my_list2]

print(len(my_list3))

