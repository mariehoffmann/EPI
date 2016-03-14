__author__ = 'Marie Hoffmann ozymandiaz147@googlemail.com'

import random

# return array with k integers from [:n], each subset and each permutation should be equally likely
# usage of randint permitted
# idea: based on Ex. 12, do not store whole array 1:n, but only swapped elements while building subset array,
# untouched elements still correspond to their index
# runtime: O(k); space: O(k)
def randomSubset(n, k):
    swapped = {}
    subset = [None for _ in range(k)] # O(k)
    for i in range(k):  # O(k)
        j = random.randint(i, n-1)  # O(1)
        val = swapped.get(j, j)     # O(1)
        swapped.update({j: swapped.get(i, i)})      # O(1)
        subset[i] = val             # O(1)
    return subset


# check uniform distribution experimentally
n = 3
k = 3
ctr = {}
for _ in range(100000):
    subset = tuple(randomSubset(n, k))
    val = ctr.get(subset, 0)
    ctr.update({subset: val+1})

for item in sorted(ctr.iteritems()):
    print item