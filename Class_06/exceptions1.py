age = input("What is your age? >")

try:
    age = int(age)

    if age > 150:
        raise Exception("Error, age must be less than 150")

    if age > 18:
        print("User can vote")
    else:
        print("Not allowed to vote")
except:
    print("An error has occurred")
