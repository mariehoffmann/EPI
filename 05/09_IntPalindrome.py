__author__ = 'Marie Hoffmann ozymandiaz147@googlemail.com'

import math

# test for palindrome of decimal represenation
def isPalindrome(x):
    digits = int(math.ceil(math.log10(x)))
    x1 = x
    while digits > 1:
        if (x1 % 10) != (x1 // 10**(digits-1)):
            return False
        x1 //= 10 # clip right
        x1 %= (x1 // 10**(digits-2))*10**(digits-2) # clip left
        digits -= 2
    return True

print(isPalindrome(33))
print(isPalindrome(13))
print(isPalindrome(32123))
print(isPalindrome(32121))
