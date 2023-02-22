countries = {'us': 'USA', 'fr': 'France', 'uk': 'England'}

# JSON

for i in countries.values():
    print(i)

for i in countries.keys():
    print(i)

for i in countries.items():
    print(f"The value for the key {i[0]} is {i[1]}.")

for k, v in countries.items():
    print(f"The value for the key {k} is {v}.")

# Does a key value exist in a dictionary?

print('fr' in countries)
p = ["aasd", "asdas", "sdfgdf"]
print("aasd" in p)


