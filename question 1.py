#Design a function that reverses the digits of an integer

def reverse_int(y):
    rev = 0
    sign = 1
    if y < 0:
        sign = -1
        y = -y
    while y != 0:
        digit = y % 10
        rev = rev * 10 + digit
        y //= 10
    return sign * rev

num = int(input("Enter an integer:"))
reversed_num = reverse_int(num)
print("The reversed integer is:", reversed_num)
