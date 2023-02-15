answer = ""

# while answer != "Q":
#     answer = input("Give a value or string, enter Q to stop")
#     if answer != "Q":
#         print(answer)

# Display the input prompt, asking for ABCD
# If the value is ok, continue on and display it later.
# If the value is unexpected, print an error like "enter the value again", and go back to ask for input.
# ----> break (at any time goes out of the loop).

# Determine the tip percentage
while True:
    answer = input("Please enter the tip amount, A B C or D")
    # if answer.upper() == "A" or answer.upper() == "B" or answer.upper() == "C" or answer.upper() == "D":
    if answer.upper() in "ABCD" and len(answer) == 1:
        break
    else:
        print("Please re-enter the value")

print("Entered tip value " + answer)

