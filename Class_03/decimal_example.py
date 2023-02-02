import decimal

value1 = decimal.Decimal("0.01")
value2 = decimal.Decimal("0.02")

print(value1 + value2)
print(type(value1))

unit_price = decimal.Decimal("8.0123")
q = decimal.Decimal("1.123")

price = unit_price * q

cents = decimal.Decimal(".01")

money_value = price.quantize(cents, decimal.ROUND_HALF_UP)
print(money_value)