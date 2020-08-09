#
# Count characters in the string
#
# count all the occurring characters in a string. 
#   - If you have a string like aba
#       - its result should be {'a': 2, 'b': 1}.
# if the string is empty? 
#   - the result should be empty object literal, {}.
def count(string):
    hash = {}
    for x in string: 
        hash[x] = hash.get(x, 0)+1
    return hash
# test.assert_equals(count('aba'), {'a': 2, 'b': 1})
# test.assert_equals(count(''), {})
# 
print(count('aba'), {'a': 2, 'b': 1})
print(count(''), {})