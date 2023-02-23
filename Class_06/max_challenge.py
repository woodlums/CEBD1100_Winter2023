def get_max1(n1, n2, n3):
    big = 0
    if n1 > n2:
        big = n1
    else:
        big = n2
    if big >= n3:
        return big
    else:
        big = n3
    return big

def get_max2(n1, n2, n3):
    max_value = n1
    if n2 > max_value:
        max_value = n2
    if n3 > max_value:
        max_value = n3
    return max_value

def get_max3(n1, n2, n3):
    if n1 > n2 and n1 > n3:
        return n1
    if n2 > n3:
        return n2
    return n3

def get_max4(n1, n2, n3):
    temp_list = [n1, n2, n3]
    temp_list.sort()
    return temp_list[-1]

print(get_max4(50, 200, 210))

