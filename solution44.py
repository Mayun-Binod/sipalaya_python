# Calculate the sum of a list of numbers using recursion
def sum_recursive(lst):
    if not lst:
        return 0
    return lst[0] + sum_recursive(lst[1:])

# Solve the Fibonacci sequence using recursion
def fib_recursive(x):
    if x <= 1:
        return x
    return fib_recursive(x - 1) + fib_recursive(x - 2)

# Calculate the sum of harmonic series up to n terms
def harmonic_recursive(m):
    if m == 1:
        return 1
    return 1 / m + harmonic_recursive(m - 1)

# Calculate the value of 'a' to the power of 'b' using recursion
def power_recursive(base, exp):
    if exp == 0:
        return 1
    return base * power_recursive(base, exp - 1)

# Find the greatest common divisor (GCD) of two integers using recursion
def gcd_recursive(num1, num2):
    if num2 == 0:
        return num1
    return gcd_recursive(num2, num1 % num2)

lst_input = [1, 2, 3, 4, 5]
print("1. Sum of list:", sum_recursive(lst_input))

fib_terms = 10
print(f"2. Fibonacci sequence up to {fib_terms} terms:")
for term in range(fib_terms):
    print(fib_recursive(term), end=" ")
print()

harmonic_terms = 5
print(f"3. Sum of harmonic series up to {harmonic_terms} terms:", harmonic_recursive(harmonic_terms))

base_num, exponent_num = 2, 3
print(f"4. {base_num} to the power of {exponent_num} is:", power_recursive(base_num, exponent_num))

gcd_num1, gcd_num2 = 56, 98
print(f"5. GCD of {gcd_num1} and {gcd_num2} is:", gcd_recursive(gcd_num1, gcd_num2))
