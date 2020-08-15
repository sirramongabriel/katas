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
def persistence(num):
    my_list = []
    y = 1
    count = 0
    str_num = str(num)
    num_length = len(str_num)
    ints = []
    num_as_list = list(str_num)

    for n in num_as_list:
        ints.append(int(n))
    
    while len(ints) > 1:
        y *= ints.pop(0)
    if len(ints) == 1:
        return ints
    # ints_length = len(ints)
    # while len(ints) > 1:
    #     for i in ints:
    #         divmod(y, i)
    #         count+=1
    # return count
    return ints

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
