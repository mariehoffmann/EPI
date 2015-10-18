__author__ = 'Marie Hoffmann ozymandiaz147@googlemail.com'

# O(x/y)
def div(x, y):
    cnt = 0
    while y < x:
        cnt += 1
        x -= y
    return cnt

# shift
def div2(x, y):
    if y > x:
        return 0
    res = 0
    while x > y:
        z = y
        cnt2 = 1
        while (z << 1) < x:
            z <<= 1
            cnt2 <<= 1
        res += cnt2
        x -= z
    return res

print(div(3,4))
print(div(30,4))
#print(div2(3,4))
print(div2(30,4))