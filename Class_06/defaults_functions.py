

def get_area(s1: float, s2: float, s3: float=None):

    if s3 is not None:
        return s1 * s2 * s3
    else:
        return s1 * s2

print(get_area(4, 5, 6))
print(get_area(5, 6))
print(get_area("A", 10))


def sample_function(a, b, c=0, d=0):
    return a + b + c + d


sample_function(2, 4, d=8)

print("Hi", end="")
print("There")


# Hint for the algorithm problems.
mytext = "I am watching TV"
my_elements = mytext.split(" ")


def describe_pet(pet_name, animal_type='dog'):
    pass


describe_pet("spot", animal_type='dolphin')

