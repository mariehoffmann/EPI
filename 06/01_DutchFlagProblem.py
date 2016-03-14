__author__ = 'Marie Hoffmann ozymandiaz147@googlemail.com'


# re-arrange array s.t. elements less than pivot appear first, followed by equal, followed by greater values
# avoids copying of arrays
# idea: use 2 pointers p_less, p_great for end of less and beginning of greater elements
#       case A_i < pivot: shuffle with successor of p_less, increment p_less
#       case A_i == pivot: leave in place, invariant: A[0:p_less] < pivot, A[p_less:i] == pivot, A[p_great:end] > pivot
#       case A_i > pivot: shuffle with last not visited element, i.e. predecessor of p_great, decrement p_great
# space: in-place, runtime: O(n)
def partition(A, p):
    pivot = A[p]
    p_less, p_great = -1, len(A)
    i = 0
    while i < len(A) and i != p_great:
        if i == p_great:
            break
        if A[i] < pivot:
            p_less += 1
            A[i], A[p_less] = A[p_less], A[i]
        elif A[i] > pivot:
            p_great -= 1
            A[i], A[p_great] = A[p_great], A[i]
            i -= 1
        i += 1


A = [3,2,1,2,3,3]
partition(A, 1)
print(A)

A = [3,3,3,3,3,1]
partition(A, len(A)-1)
print(A)
