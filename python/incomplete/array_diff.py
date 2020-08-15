#
# Array.diff
#
# Goal: 
#     - implement a difference function, 
#         - which subtracts one list from another 
#         - and returns the result.
#     - It should remove all values from list a, which are present in list b.
# Explanation:
#     - array_diff([1,2],[1]) == [2]
#     - If a value is present in b, all of its occurrences must be removed from the other:
#     - array_diff([1,2,2,2,3],[2]) == [1,3]
# import numpy as np
def array_diff(a, b):
    arr1 = list(dict.fromkeys(a))
    arr2 = list(dict.fromkeys(b))
    result = []
    for i in arr1:
        if i not in arr2:
            result.append(i)
    return result
# Test.assert_equals(array_diff([1,2], [1]), [2], "a was [1,2], b was [1], expected [2]")
# Test.assert_equals(array_diff([1,2,2], [1]), [2,2], "a was [1,2,2], b was [1], expected [2,2]")
# Test.assert_equals(array_diff([1,2,2], [2]), [1], "a was [1,2,2], b was [2], expected [1]")
# Test.assert_equals(array_diff([1,2,2], []), [1,2,2], "a was [1,2,2], b was [], expected [1,2,2]")
# Test.assert_equals(array_diff([], [1,2]), [], "a was [], b was [1,2], expected []")
print(array_diff([1,2], [1]))    # [2], "a was [1,2], b was [1], expected [2]"
print(array_diff([1,2,2], [1]))  # [2,2], "a was [1,2,2], b was [1], expected [2,2]"
print(array_diff([1,2,2], [2]))  # [1], "a was [1,2,2], b was [2], expected [1]"
print(array_diff([1,2,2], []))   # [1,2,2], "a was [1,2,2], b was [], expected [1,2,2]"
print(array_diff([], [1,2]))     # [], "a was [], b was [1,2], expected []"
