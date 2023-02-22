GST = 0.05

# Calculate the standard Quebec tax for "price".
def calculate_tax(price):
    tax = price * 0.09975
    tax += price * GST # 0.05
    return tax

cost = 100.00

# print (cost + calculate_tax(cost))
print(f"The amount of tax for {cost} is {calculate_tax(cost)}")


# price = 210.00
#
# tax = price
# tax += price * 0.09975
# tax += price * 0.05
#
# print (tax)
