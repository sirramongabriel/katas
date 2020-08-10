#
# Does the String end with?
#
# Complete the solution 
#   - return true if the first argument ends w/ the 2nd.
#       - both args are strings
#
# Examples:
# solution('abc', 'bc') # returns true
# solution('abc', 'd') # returns false
#
# test.assert_equals(solution('abcde', 'cde'), True)
# test.assert_equals(solution('abcde', 'abc'), False)
# test.assert_equals(solution('abcde', ''), True)
#
def solution(start, end):
    length = len(end)

    return len(end)

    # if start[-length]==end:
    #     return True
    # else: 
    #     return False
print(solution('abcde', 'cde')) # True
print(solution('abcde', 'abc')) # False
print(solution('abcde', ''))    # True