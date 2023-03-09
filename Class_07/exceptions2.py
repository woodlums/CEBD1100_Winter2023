import sys

try:

    age = input("What is your age? >")

    age = int(age)

    if age == 5:
        pass

    assert age <= 150 and age > 0, "Error, age must be less than 150"

    if age > 18:
        print("User can vote")
    else:
        print("Not allowed to vote")

    exit(0)

except AssertionError as e:

    print("An error has occurred:" + str(e))

    exit(1)

except (ValueError, ZeroDivisionError) as e:

    # A system error has occurred, please contact support with this ID number: 202303081904-000001

    print(str(e))
    print("Sorry, the input you gave is in the incorrect format, and can't be 0.")

except Exception as e:
    # LOG EXCEPTION TO FILE
    print("An unknown error has occurred.")
