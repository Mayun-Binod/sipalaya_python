# operators in python

#1.arithmetic operator
# +(add),-(sub),%(modulo operator),**(exponent operator),/(div),*(mul),//(floor division)
num1 = 10
num2 = 3

print(num1 + num2)  # Addition: 13
print(num1 - num2)  # Subtraction: 7
print(num1 * num2)  # Multiplication: 30
print(num1 / num2)  # Division: 3.33
print(num1 // num2) # Floor division: 3
print(num1 % num2)  # Modulo: 1
print(num1 ** num2) # Exponent: 1000

# 2.Assignment operator
# =,+=,-=,/=,%=,//=,*=,**=
value = 5
value += 3   # Same as value = value + 3
print(value) # 8

value -= 2   # Same as value = value - 2
print(value) # 6

value *= 2   # Same as value = value * 2
print(value) # 12

value //= 3  # Same as value = value // 3
print(value) # 4

value %= 2   # Same as value = value % 2
print(value) # 0


# 3.comparison operator
# used to combine two or more values
# gives output in boolean
# >,<,==,<=,>=,!=
num1 = 10
num2 = 20

print(num1 > num2)   # False
print(num1 < num2)   # True
print(num1 == num2)  # False
print(num1 != num2)  # True
print(num1 >= 10)    # True
print(num2 <= 15)    # False


# 4.membership operator
# in operator gives true or false
# not operator gives true or false
my_list = [1, 2, 3, 4]

print(2 in my_list)    # True
print(5 not in my_list) # True

# 5.identity operator
# is also check memory location
# is not  also check memory location
list_a = [1, 2, 3]
list_b = [1, 2, 3]
list_c = list_a

print(list_a is list_c)      # True (same memory location)
print(list_a is list_b)      # False (different memory location)
print(list_a is not list_b)  # True

# 6. logical operator
# and
# or
# not
flag1 = True
flag2 = False

print(flag1 and flag2)  # False
print(flag1 or flag2)   # True
print(not flag1)        # False


# 7.bitwise operator
# and (&),or(|), not (~),>> (right shift),<<(left shift)

num1 = 5  # 0101 in binary
num2 = 3  # 0011 in binary

print(num1 & num2)  # 1 (0101 & 0011 = 0001)
print(num1 | num2)  # 7 (0101 | 0011 = 0111)
print(~num1)        # -6 (bitwise not: ~0101 = 1010 in two's complement)
print(num1 << 1)    # 10 (left shift: 0101 << 1 = 1010)
print(num1 >> 1)    # 2 (right shift: 

