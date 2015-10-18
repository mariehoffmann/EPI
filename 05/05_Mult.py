__author__ = 'Marie Hoffmann ozymandiaz147@googlemail.com'

# assume 64 bit integer
def add(a, b):
    if a == 0:
        return b
    if b == 0:
        return a
    c = a^b
    cf = 0
    # test carry forward
    for i in range(64):
        bit_mask = 1 << i
        if cf == 1 & (c & bit_mask) == 0:
            c |= bit_mask
        if ((bit_mask & a) | (bit_mask & b)) == 0:
            continue
        cf = 1
    return c

# define multiplication with =, ==, |, &, ^, <<, >> only
# idea: i) extract left-most bit bitL of x, ii) shift y by bitL, iii) clear bitL and go to i)
def mult(x, y):
    prod = 0
    while True:
        if x == 0:
            break
        bitL = x & ~(x-1) # decimal presentation!
        z = y
        #print("bitL = {:d}".format(bitL))
        while True:
            if bitL == 1:
                break
            z <<= 1
            bitL >>= 1
        prod = add(prod, z)
        x &= (x-1)
    return prod


print(add(0,6))
print(add(2,1))
print(mult(2,7))