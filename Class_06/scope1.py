b = 5

def add_1():
    global b
    b = b + 1 # Local scope within this function.

add_1()

print(b)

