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
    end_length = (len(end)*-1)
    start_length = len(start)
    int_end_length = int(end_length)
    if start[end_length:] == end:
        return True
    elif end == '':
        return True
    else:
        return False
print(solution('abcde', 'cde')) # True
print(solution('abcde', 'abc')) # False
print(solution('abcde', ''))    # True
#
# Notes: 
# Python slice
#
# a[start:stop]  # items start through stop-1
# a[start:]      # items start through the rest of the array
# a[:stop]       # items from the beginning through stop-1
# a[:]           # a copy of the whole array
#