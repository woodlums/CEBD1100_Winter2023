# Print a square based on a size variable using *
# Rules:  Don't multiply the string
# Print a triangle based on size.

# HINT - You probably need two 'for' loops to make this work.

# End-time : 7:30

# Size of the square or triangle drawn.
SIZE = 5

###
###
###

# for y in range(SIZE): # LINE (Y)
#     for x in range(SIZE):
#         print("*", end="")
#     print("")

PRINT_VALUE = "*"

for y in range(SIZE): # LINE (Y)
    for x in range(y+1):
        print(PRINT_VALUE, end="")
    print("")

#
##
###

# print("1\t2\t3")