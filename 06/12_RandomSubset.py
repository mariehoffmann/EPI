__author__ = 'Marie Hoffmann ozymandiaz147@googlemail.com'

import random

# create random subset of size k from A and store it in A
# idea: build permutation P[:k] = unique random idcs , P[k:] = identity
# runtime: O(k) sampling and application of first k permutation mappings
# space: O(k)
def rndSubset(A, k):
    idcs = random.sample(xrange(len(A)), k)
    for i in range(k):
        A[i], A[idcs[i]] = A[idcs[i]], A[i]

# improve space by drawing random element to swap with current i = [1:k]
# runtime O(k)
# space O(1)
def rndSubset2(A, k):
    for i in range(k):
        idx = random.randint(i, len(A)-1)
        A[i], A[idx] = A[idx], A[i]

A = [6, 2, 3, 5, 4, 1, 0]
k = 3
print "A = ", A
rndSubset(A, k)
print "Subset of size ", k, " is ", A[:k], " and rest ", A[k:]

print "A = ", A
rndSubset2(A, k)
print "Subset of size ", k, " is ", A[:k], " and rest ", A[k:]

