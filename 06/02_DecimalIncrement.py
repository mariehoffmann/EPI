__author__ = 'Marie Hoffmann ozymandiaz147@googlemail.com'


# D = (x,y,z) -> D+1, tuple represent arbitrary decimal
def increment(D):
    D1 = []
    cf = 1
    for i, num in enumerate(reversed(D)):
        if cf == 1:
            if num < 9 or i == len(D)-1:
                num += 1
                cf = 0
            else:
                num = 0
        D1.append(num)
    D1.reverse()
    if D1[0] == 10: # split leading two digit num
        D1 = [1,0] + D1[1:]
    return tuple(D1)

# Variant: receive strings s,t representing binary numbers B_t, B_s, return string representing B_t+B_s
def binaryAddition(s, t):
    n = max(len(s), len(t))+1
    # prepend zeros for shorter string
    s = ''.join(['0' for _ in range(max(1, n-len(s)))]) + s
    t = ''.join(['0' for _ in range(max(1, n-len(t)))]) + t
    u = ['0' for _ in range(n)]
    cf = 0
    for i in reversed(range(n)):
        if s[i] == t[i] == '1':
            u[i] = str(cf + 0)
            cf = 1
        elif s[i] == t[i] == '0':
            if cf == 1:
                u[i] = '1'
                cf = 0
            else:
                u[i] = '0'
        else: # and s_i or s_t is 1!
            if cf == 1:
                u[i] = '0'
            else:
                u[i] = '1'
    # remove leading 0
    if u[0] == '0':
        del u[0]
    return ''.join(u)


print(increment((1,2,3)))
print(increment((1,2,9)))
print(increment((1,9,9)))
print(increment((9,9,9)))

print(binaryAddition('0', '1'))
print(binaryAddition('1', '1'))
print(binaryAddition('1', '11'))




