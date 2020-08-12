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
import numpy as np
def persistence(num):
    my_list = []
    count = 0
    second_count = 0
    str_num = str(num)
    num_length = len(str_num)
    count = num_length
    while count > 0:
        for i in str_num:
            my_list.append(int(i))
            count-=1
            
    result = np.prod(np.array(my_list)) 
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
print(persistence(4))   # 0
print(persistence(25))  # 2
print(persistence(999)) # 4
