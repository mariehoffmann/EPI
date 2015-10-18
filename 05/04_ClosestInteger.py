__author__ = 'Marie Hoffmann ozymandiaz147@googlemail.com'

# closest integer with same weight (sum of bits)
# extract lowest one bit, invert lowest 0 by working on complement
def closestInt(x):
    lowest = x & ~(x-1)
    y = ~(~x & (~x-1))
    return y-lowest


print(closestInt(5))
print(closestInt(3))
print(closestInt(2))