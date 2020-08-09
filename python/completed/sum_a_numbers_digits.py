# Write a function named sumDigits 
#   - takes a number as input 
#   - returns the sum of the absolute value of each of the number's decimal digits. 
# 
# Example:
#   - sum_digits(10)  # Returns 1
#   - sum_digits(99)  # Returns 18
#   - sum_digits(-32) # Returns 5
#
# Note: 
#   - all numbers in the input will be integers.
import math
def sumDigits(number):
    abs_num = abs(number)
    string_num = str(abs_num)
    array = []
    for x in string_num:
        array.append(int(x))
    return sum(array)
#
# test.assert_equals(sum_digits(10), 1)
# test.assert_equals(sum_digits(99), 18)
# test.assert_equals(sum_digits(-32), 5)
#
print(sumDigits(10))  # 1
print(sumDigits(99))  # 18
print(sumDigits(-32)) # 5
