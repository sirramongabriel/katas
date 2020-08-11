#
# Factorial
#
# In mathematics, the factorial of a positive integer n, is the product of all positive integers less than or equal to n
#     - example: 5! = 5 * 4 * 3 * 2 * 1 = 120
#     - by convention the value of 0 is 1
#
# Write a function to calculate factorial for a given input.
#   - if input is below 0 or above 12 throw a ValueError exception(Python) 
#
# Note: 
#   - More details about factorial can be found at: https://www.wikiwand.com/en/Factorial
def factorial(number): 
    result = 1
    if number < 0 or number > 12:
        raise ValueError('Number must be between 1 & 11')
    elif number == 0:
        return 1
    elif number == 1: 
        return 1
    else:
        for i in range(number, 0, -1):
            result *= i 
        return result
#
# Test.assert_equals(factorial(0), 1, "factorial for 0 is 1");
# Test.assert_equals(factorial(1), 1, "factorial for 1 is 1");
# Test.assert_equals(factorial(2), 2, "factorial for 2 is 2");
# Test.assert_equals(factorial(3), 6, "factorial for 3 is 6");
#
print(factorial(0)) # "factorial for 0 is 1"
print(factorial(1)) # "factorial for 1 is 1"
print(factorial(2)) # "factorial for 2 is 2"
print(factorial(3)) # "factorial for 3 is 6"