#
#   Sum of a sequence
#
# create a function, which returns the sum of a sequence of integers.
#   - sequence is defined by 3 non-negative values: 
#       - start 
#       - end 
#       - step
#   - if start value is greater than the end, 
#       - function should return 0
#
# Examples:
#
# sequenceSum(2,2,2) === 2
# sequenceSum(2,6,2) === 12 // 2 + 4 + 6
# sequenceSum(1,5,1) === 15 // 1 + 2 + 3 + 4 + 5
# sequenceSum(1,5,3) === 5 // 1 + 4
def sequence_sum(start, end, step):
    numbers = []
    result = 0
    end = end+1
    for i in range(start, end, step):
        numbers.append(i)
    for n in numbers:
        result += n
    return result
#
# Test.assert_equals(sequence_sum(2, 6, 2), 12)
# Test.assert_equals(sequence_sum(1, 5, 1), 15)
# Test.assert_equals(sequence_sum(1, 5, 3), 5)
# Test.assert_equals(sequence_sum(0, 15, 3), 45)
# Test.assert_equals(sequence_sum(16, 15, 3), 0)
# Test.assert_equals(sequence_sum(2, 24, 22), 26)
# Test.assert_equals(sequence_sum(2, 2, 2), 2)
# Test.assert_equals(sequence_sum(2, 2, 1), 2)
# Test.assert_equals(sequence_sum(1, 15, 3), 35)
# Test.assert_equals(sequence_sum(15, 1, 3), 0)
#
print(sequence_sum(2, 6, 2))   # 12
print(sequence_sum(1, 5, 1))   # 15
print(sequence_sum(1, 5, 3))   # 5
print(sequence_sum(0, 15, 3))  # 45
print(sequence_sum(16, 15, 3)) # 0
print(sequence_sum(2, 24, 22)) # 26
print(sequence_sum(2, 2, 2))   # 2
print(sequence_sum(2, 2, 1))   # 2
print(sequence_sum(1, 15, 3))  # 35
print(sequence_sum(15, 1, 3))  # 0