# Write a function, persistence, 
#     - takes in a positive num 
#     - returns its multiplicative persistence, 
#         - which is the # of times you must multiply the digits in num until you reach a single digit.

# Examples:
#  persistence(999) => 4 # Because 9*9*9 = 729, 7*2*9 = 126, 1*2*6 = 12 & finally 1*2 = 2.
#  persistence(4)   => 0  because 4 is already a one-digit number.
#  persistence(39)  => 3, because 3*9=27, 2*7=14, 1*4=4 & 4 has only one digit
#  persistence(999) => 4, because 9*9*9=729, 7*2*9=126, 1*2*6=12 & finally 1*2=2
#  persistence(4)   => 0, because 4 is already a one-digit number
# 
# Source: https://codereview.stackexchange.com/questions/156769/repeatedly-multiplying-digits-until-a-single-digit-is-obtained#
from functools import reduce
import operator
def persistence(num):
    string = str(num)
    str_digits = []
    ints = []
    result = 1
    for i in string:
        str_digits.append(i)
    for d in str_digits:
        ints.append(int(d))
    while result > 9:
        result = reduce(lambda x, y: x*y, ints)
        str_digits.append(str(result))
        for d in str_digits:
            ints.append(int(d))
    return result
#
# Tests: 
    # print("Basic tests")
    # Test.assert_equals(persistence(39), 3)
    # Test.assert_equals(persistence(4), 0)
    # Test.assert_equals(persistence(25), 2)
    # Test.assert_equals(persistence(999), 4)
# print("Basic tests")
print(persistence(39))  # 3
# print(persistence(4))   # 0
# print(persistence(25))  # 2
# print(persistence(999)) # 4
