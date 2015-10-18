__author__ = 'Marie Hoffmann ozymandiaz147@googlemail.com'


def rev(x):
    x_str = [c for c in str(x)]
    x_str.reverse()
    return int(''.join(x_str))

# without string conversion
def rev2(x):
    sign = 0
    if x < 0:
        sign = 1
        x = abs(x)
    y = 0
    dec = 0
    while x > 0:
        y = y*10 + x % 10
        x //= 10
    return y*(-1)**sign

print(rev(10))
print(rev(1413))

print(rev2(10))
print(rev2(1413))