def canvote(age: int):
    # if age > 18:
    #     return True

    return age > 18


def addnumsover(limit = 0, num1 = 0, num2 = 0, num3 = 0):


    total = 0

    if num1 > limit:
        total += num1
    if num2 > limit:
        total += num2
    if num3 > limit:
        total += num3
    return total

# limit -> 3
# num2

print(addnumsover(num2=4, limit=3))



def describe_pet(pet_name, animal_type='dog'):
    print(f"Your pet name is {pet_name} and it is a {animal_type}")

print(describe_pet("Spot"))

# subroutine