__author__ = 'Marie Hoffmann ozymandiaz147@googlemail.com'

import sys

# return True if it's possible to advance from A_0 to A_end given A_i the maximum number of steps one can forward
def advance(A):
    mf = A[0] # max forward
    for i in range(1, len(A)):
        if mf < i:
            return False
        mf = max(mf, i+A[i])
    return True

# Variant: minimal number of skips from A_0 to A_end, O(n^2)
# idea: from all predecessors
def advanceMin(A):
    d = [sys.maxint for _ in range(len(A))]
    d[0] = 0
    mf = [a + i for i, a in enumerate(A)]
    for i in range(1, len(A)):
        if i > max(mf[:i]):
            return -1
        d[i] = min([d_j for j, d_j in enumerate(d[:i]) if mf[j] >= i]) + 1
    return d[-1]

print(advance([3,3,1,0,2,0,1]))
print(advance([3,2,0,0,2,0,1]))

print(advanceMin([3,3,1,0,2,0,1]))
print(advanceMin([3,2,0,0,2,0,1]))


