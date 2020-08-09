#
# Anagram Detection
#
# An anagram is the result of rearranging the letters of a word to produce a new word (see wikipedia).
#   - anagrams are case insensitive
# Complete the function 
#   - return true if the two arguments given are anagrams of each other
#   - return false otherwise.
# Examples:
#   - "foefet" is an anagram of "toffee"
#   - "Buckethead" is an anagram of "DeathCubeK"
#
# Algo:
#   - Given two words
#   - Do they contain the same characters?
#       - sort the characters
#       - check if all characters match between words
#       - check if character count is the same in both words
import collections

def is_anagram(test, original):
    test_chars = list(test)
    original_chars = list(original)
    # sorted_test = test_chars.sort()
    # sorted_original = original_chars.sort()
    test_downcased = []
    original_downcased = []
    for char in test_chars:
        test_downcased.append(char.lower())
    for char in original_chars:
        original_downcased.append(char.lower())
    if collections.Counter(test_downcased) == collections.Counter(original_downcased):
        return True
    else:
        return False
# Test.assert_equals(is_anagram('Creative', 'Reactive'), True, 'The word Creative is an anagram of Reactive')
# Test.assert_equals(is_anagram("foefet", "toffee"), True, 'The word foefet is an anagram of toffee')
# Test.assert_equals(is_anagram("Buckethead", "DeathCubeK"), True, 'The word Buckethead is an anagram of DeathCubeK')
# Test.assert_equals(is_anagram("Twoo", "WooT"), True, 'The word Twoo is an anagram of WooT')
# Test.assert_equals(is_anagram("dumble", "bumble"), False, 'Characters do not match for test case dumble, bumble')
# Test.assert_equals(is_anagram("ound", "round"), False, 'Missing characters for test case ound, round')
# Test.assert_equals(is_anagram("apple", "pale"), False, 'Same letters, but different count')

print(is_anagram('Creative', 'Reactive'))      # True, 'The word Creative is an anagram of Reactive')
print(is_anagram("foefet", "toffee"))          # True, 'The word foefet is an anagram of toffee')
print(is_anagram("Buckethead", "DeathCubeK"))  # True, 'The word Buckethead is an anagram of DeathCubeK')
print(is_anagram("Twoo", "WooT"))              # True, 'The word Twoo is an anagram of WooT')
print(is_anagram("dumble", "bumble"))          # False, 'Characters do not match for test case dumble, bumble')
print(is_anagram("ound", "round"))             # False, 'Missing characters for test case ound, round')
print(is_anagram("apple", "pale"))             # False, 'Same letters, but different count')