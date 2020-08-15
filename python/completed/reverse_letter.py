#
# Reverse Letter
#
# Task:
#     - given a string str, 
#         - reverse it 
#         - omitting all non-alphabetic characters.

# Example:
#     - for str = "krishan", the output should be "nahsirk".
#     - for str = "ultr53o?n", the output should be "nortlu".

# Input/Output:
#     - [input] string str
#         - the string consists of lowercase latin letters, digits and symbols.
#     - [output] a string
#
def reverse_letter(string):
    letters = []
    result = ''
    for x in string:
        if x.isalpha():
            letters.append(x)
    letters.reverse()
    result = ''.join(letters)
    return result
# Test.assert_equals(reverse_letter("krishan"),"nahsirk")
# Test.assert_equals(reverse_letter("ultr53o?n"),"nortlu")
# Test.assert_equals(reverse_letter("ab23c"),"cba")
print(reverse_letter("krishan"))   # "nahsirk"
print(reverse_letter("ultr53o?n")) # "nortlu"
print(reverse_letter("ab23c"))     # "cba"