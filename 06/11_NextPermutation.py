__author__ = 'Marie Hoffmann ozymandiaz147@googlemail.com'


# compute next permutation under dictionary ordering,
# i.e. search for first not reversed ordered neighbours from right to left
# if not found return empty list, runtime: O(n), space: O(1)
def nextPermutation(A):
    for i in reversed(range(1,len(A))):
        if A[i] > A[i-1]: # swap with 1st larger elem in suffix
            i2 = min(filter(lambda item: item[1] > A[i-1], enumerate(A[i:], start=i)), key=lambda item: item[1])[0]
            A[i-1], A[i2] = A[i2], A[i-1]
            # suffix still sorted in decreasing order -> minimize (= reverse)
            A[i:] = reversed(A[i:])
            return
    del A[:]

# variation: compute preceeding permutation under dictionary ordering,
# search first non increasing pair from right to left, swap with largest smaller element in suffix and
# minimize suffix
def previousPermutation(A):
    for i in reversed(range(1, len(A))):
        if A[i-1] > A[i]: # swap with largest smaller value
            i2 = max(filter(lambda item: item[1] < A[i-1], enumerate(A[i:], start=i)), key=lambda item: item[1])[0]
            A[i-1], A[i2] = A[i2], A[i-1]
            # maximize suffix, i.e. reverse increasing ordering
            A[i:] = reversed(A[i:])
            return
    del A[:] # else return empty list

A = [8, 5, 3]
print "Permutation = \t", A
nextPermutation(A)
print "next Permuation = \t", A

A = [6, 2, 3, 5, 4, 1, 0]
print "Permutation = \t", A
nextPermutation(A)
print "next Permuation = \t", A

previousPermutation(A)
print "previous Permuation = \t", A












