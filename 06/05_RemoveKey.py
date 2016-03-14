__author__ = 'Marie Hoffmann ozymandiaz147@googlemail.com'

# remove key without using library deletion functions, return new length
# idea: shuffle elements to last position and decrease length
def removeKey(A, key):
    l = len(A)
    i =  0
    while i < l:
        if A[i] == key:
            A[i], A[l-1] = A[l-1], A[i]
            print(A)
            l -= 1
        else:
            i += 1
    return A, l

A = [3,2,3,2]
print(removeKey([3,2,3,2], 3))
print(removeKey([3,2,3,2], 1))
print(removeKey([1], 1))


