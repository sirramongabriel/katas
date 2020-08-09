#
#   Count the divisiors of a number
#
#   Count the number of divisors of a positive integer n.
#       - Random tests go up to n = 500000.
#
def divisors(n):
    divisors = []
    for i in range (1, (n+1)):
        if n % i == 0:
            divisors.append(i)
    return len(divisors)
# 
#   Tests:
#
#   Test.assert_equals(divisors(4), 3)
#   Test.assert_equals(divisors(5), 2)
#   Test.assert_equals(divisors(12), 6)
#   Test.assert_equals(divisors(30), 8)
#   Test.assert_equals(divisors(4096), 13)
print divisors(4)
print divisors(5)
print divisors(12)
print divisors(30)
print divisors(4096)