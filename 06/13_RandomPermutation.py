__author__ = 'Marie Hoffmann ozymandiaz147@googlemail.com'

import random
import copy

# swap i-th element with random element from suffix
# time O(n), space O(1)
def randomPermutation(A):
    for i in range(len(A)-1):
        j = random.randint(i, len(A)-1)
        A[i], A[j] = A[j], A[i]


# count permutations to see their uniform distributions
A = range(3)
c = {}
for _ in range(100000):
    B = copy.copy(A)
    randomPermutation(B)
    ctr = c.get(tuple(B), 0)
    c.update({tuple(B): ctr+1})
ctr_sum = sum(c.values())
for item in c.iteritems():
    c.update({item[0]: item[1]/float(ctr_sum)})

print c

