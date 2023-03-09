shopping_list= [123, 123, 444, 432, 221, 444]
store_inventory= {123: ("Tea", 4.99), 444: ("Coffee", 16.99), 432: ("Juice", 3.99), 221: ("Aero Bar", 1.19), }

total = 0

for key in store_inventory:

    count_items = shopping_list.count(key)

    multiple_str = ''
    multiple_amount = ''

    if count_items > 1:
        multiple_str = "x"+str(count_items)
        multiple_amount = '$' + str(count_items*store_inventory[key][1])

    print('{0:10}'.format(store_inventory[key][0]), '$' + '{0:5}'.format(str(store_inventory[key][1])),
          multiple_str, multiple_amount)
    total += store_inventory[key][1]*count_items

print("=" * 30)
print('{0:10}'.format("Total"), '$'+str(round(total,2)))
