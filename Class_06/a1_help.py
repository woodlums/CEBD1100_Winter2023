import decimal

# Get the amount for the meal.

while True:

    meal_price = input("What is the price of the meal? >")

    if meal_price.isdecimal():
        print("OK")
        break

    print("Not ok")

    # try:
    #     meal_price = decimal.Decimal(meal_price)
    #     break
    # except:
    #     print("Sorry, your input was not correct.")


print(f"Thank you for the price, it was {meal_price}")


