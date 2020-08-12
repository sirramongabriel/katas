#
# Highest & Lowest
#
# given a string of space separated numbers, 
#   - return the highest & lowest number
#   - return value order highest then lowest
#   - numbers are separated by a space
#
# Example:
#   - high_and_low("1 2 3 4 5")  # return "5 1"
#   - high_and_low("1 2 -3 4 5") # return "5 -3"
#   - high_and_low("1 9 3 4 -5") # return "9 -5"
# Notes:
#   - all numbers are valid Int32, no need to validate them.
#   - there is at least one number in the input string.
#   - output string must be two numbers separated by a single space
#   - highest number is first
def high_and_low(string):
    highest = ""
    lowest  = ""
    arr = string.split()
    ints = []
    for i in arr:
        ints.append(int(i))
    sorted_str = sorted(ints, key=None, reverse=True)
    highest = sorted_str[0]
    lowest = sorted_str[-1]
    result = "{} {}".format(highest, lowest)
    return result
#
# Test.assert_equals(high_and_low("4 5 29 54 4 0 -214 542 -64 1 -3 6 -6"), "542 -214");
print(high_and_low("4 5 29 54 4 0 -214 542 -64 1 -3 6 -6")) # "542 -214"