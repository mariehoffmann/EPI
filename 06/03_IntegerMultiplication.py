__author__ = 'Marie Hoffmann ozymandiaz147@googlemail.com'

# x, y are arbitrary integer precision tuples, leading digit may be negative
# (-3,1)*(2,0) returns (-6,2,0), start with (y_0*x)*10**(len(y)-1)
def mult(x, y):
    x = [int(d) for d in str(x)]
    y = [int(d) for d in str(y)]
    # 1. sum up partial products
    tmp = [0 for _ in range(len(x))]
    for j, d_y in enumerate(y):
        cf = 0
        for i, d_x in enumerate(x):
            tmp[i] += d_x*d_y*10**(len(y)-1-j)
    # 2. normalize
    cf = 0
    for i in reversed(range(len(x))):
        d_new = tmp[i] + cf
        tmp[i] = d_new % 10
        cf = d_new // 10
    if cf > 0:
        tmp = [cf] + tmp
        while tmp[0] > 9:
            cf = tmp[0] // 10
            tmp[0] %= 10
            tmp = [cf] + tmp
    return tuple(tmp)

print(mult((32), (20)))
print(mult((32), (200)))
print(mult((32), (0)))
print(mult((9), (99)))