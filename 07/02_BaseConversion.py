__author__ = 'Marie Hoffmann ozymandiaz147@googlemail.com'

'''
    Write program that receives a string representing an integer of base b1 and returns a string
    representing the same number in base b2 where 2 <= b1, b2 <= 16.
'''

import math

def base_conversion(s, b1, b2):
    if s == '0':
        return str(b2) + 'x' + s
    s2 = ''
    # convert string to int in decimal representation
    d10 = 0
    sign = '-' if s[0] == '-' else ''
    s = s[1:] if ord(s[0]) < 48 else s
    for d in s:
        d10 = d10*b1 + ord(d)
        d10 = (d10 - ord('0')) if ord(d) <= ord('9') else (d10 - ord('A'))
    nd = int(1+math.log(d10)/max(1, math.log(b2)))  # number of digits
    po = b2**nd
    for i in range(nd, -1, -1):
        digit_b2 = d10//po
        s2 += str(digit_b2) if digit_b2 < 10 else unichr(digit_b2-10+ord('A'))
        d10 %= po
        po /= b2
    return sign + str(b2) + 'x' + s2


print base_conversion('0', 2, 3)
print base_conversion('11011', 2, 3)
print base_conversion('1000', 3, 2)
print base_conversion('11011', 2, 16)
print base_conversion('-01B', 16, 8)



