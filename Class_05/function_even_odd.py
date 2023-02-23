# Create a fcn that specifies even or odd.

# Input?  An integer.
# Output? "even" "odd" --- True / False

def is_even(num):
    return num % 2 == 0

def is_even2(number):
    return not number % 2

print(is_even(3))