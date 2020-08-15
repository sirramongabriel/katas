#
# Form the minimum number
#
# Task:
#   -given a list of digits, return the smallest number that could be formed from these digits, 
#   - using the digits only once 
#       - ignore duplicates
#
# Notes:
#   - only positive integers will be passed to the function (> 0 ), no negatives or zeros.
# Examples:
#   - minValue ([1, 3, 1])  ==> return (13)
#       - (13) is the minimum number could be formed from [1, 3, 1] , Without duplications
#   - minValue([5, 7, 5, 9, 7])  ==> return (579)
#       - (579) is the minimum number could be formed from [5, 7, 5, 9, 7] , Without duplications
#   - minValue([1, 9, 3, 1, 7, 4, 6, 6, 7]) return  ==> (134679)
#       - (134679) is the minimum number could be formed from [1, 9, 3, 1, 7, 4, 6, 6, 7] , Without duplications
# TODO: 
#   - remove duplicates from list
#   - sort unique numbers list from least to greatest
#   - join unique numbers as a string
#   - return string number as an integer
def min_value(digits):
    str_list = []
    stringulator = ""
    d_list = list(dict.fromkeys(digits))
    sorted_list = sorted(d_list)
    for s in sorted_list:
        stringulator += "{}".format(s)
    result = int(stringulator)
    return result
#
# Test.assert_equals(min_value([1, 3, 1]), 13)
# Test.assert_equals(min_value([4, 7, 5, 7]), 457)
# Test.assert_equals(min_value([4, 8, 1, 4]), 148)
#
print(min_value([1, 3, 1]))     # 13
print(min_value([4, 7, 5, 7]))  # 457
print(min_value([4, 8, 1, 4]))  # 148
