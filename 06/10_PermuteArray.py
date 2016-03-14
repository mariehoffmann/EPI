__author__ = 'Marie Hoffmann ozymandiaz147@googlemail.com'

import timeit
import numpy as np

# idea 1: sort [(a_i, p_i), key=p], runtime: O(nlogn), space: O(n)
# A     array of elements to permute, P     index mapping
def permuteArray(A, P):
    AP = zip(A, P)
    AP.sort(key=lambda ap: ap[1])
    return [ap[0] for ap in AP]

# idea 2: apply mapping and store in new array: runtime O(n), space: O(n)
def permuteArray2(A, P):
    A_new = [None for _ in range(len(A))]
    for i in range(len(A)):
        A_new[P[i]] = A[i]
    return A_new

# idea 3: apply permutation iteratively in-place, i.e. copy A[i] to A[P[i]] together with P[i] to P[P[i]],
# save former A[P[i]] and P[P[i]] and apply moving in next round, since P is permutation each address i is used once
# runtime: O(n), space: O(1)
def permuteArray3(A, P):
    a = A[0]
    p = P[0]
    j = 0
    for i in range(len(A)):
        while p == P[p] and j < len(A)-1:
            j += 1
            p = P[j]
            a = A[j]
        a_next = A[p]
        p_next = P[p]
        A[p] = a
        P[p] = p
        a = a_next
        p = p_next
    #return A



A = [chr(i) for i in range(97,97+26)]
P = np.random.permutation(len(A))

start = timeit.default_timer()
B = permuteArray(A, P)
stop = timeit.default_timer()

print "permute array with sorting: ", stop - start
print B

start = timeit.default_timer()
B = permuteArray2(A, P)
stop = timeit.default_timer()

print "permute array with copying to 2nd array: ", stop - start
print B

start = timeit.default_timer()
permuteArray3(A, P)
stop = timeit.default_timer()

print "permute array with cycling copying: ", stop - start
print A


