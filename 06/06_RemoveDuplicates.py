__author__ = 'Marie Hoffmann ozymandiaz147@googlemail.com'

'''
    Remove duplicates in sorted array, s.t. elements are shifted right
    Return length of new list, rest of array may contain arbitrary elements
     Idea: two iterating pointers i for current position, j for next valid entry (no duplicate of previous entries)
      shuffle a[i+1] and a[j] if a[i+1] contains value less (in later iterations) or equal to a[i]
    Runtime: O(n), space: O(1)
'''

def remove_duplicates(a):
    i,j = 0,1
    while j < len(a):
        # move j to next valid entry larger than a[i]
        while j < len(a) and a[i] >= a[j]:
            j += 1
        # shuffle if there are duplicates in between
        if j < len(a) and j > i+1:
            aux = a[i+1]
            a[i+1] = a[j]
            a[j] = aux
        i += 1
        j += 1
    return i+1

def remove_duplicates2(a):
    p1, p2, n = 0, 1, len(a)
    while p1 < n and p2 < n:
        if a[p1] == a[p2]:
            while p2 < n and a[p1] == a[p2]:
                p2 += 1
            if p2 < n:
                a[p1+1] = a[p2]
        p1 += 1
        p2 += 1

    return p1

def remDup(A):
    i,j, l = 0, 1, len(A)
    while i < j < l:
        if A[i] >= A[j]:
            while j < l and A[j] <= A[i]:
                j += 1
            A[i+1] = A[j]
        i += 1
        j += 1
    return A, i+1

# variant: update all occurances of x in A if x occurs exactly m times, s.t. |x in A'| == min(2,m)
# A is sorted, single pass, no additional space
def redDup(A, m):
    s, t, l = -1, 0, len(A)
    while s < t < l:
        s += 1
        t += 1
        if t + 1 < l and A[s] == A[t+1]:
            s += 1
            while t < l and A[s] == A[t]:
                t += 1
        if t < l:
            A[s+1] = A[t]
    return A, s+1


if __name__ == "__main__":
    # expect 3
    # a = [5,5,5,7,8,8]
    # print(str(remove_duplicates2(a)))
    # # expect 6
    # a = list(range(6))
    # print(str(remove_duplicates2(a)))
    #
    #
    # a = [5,5,5,7,8,8,9]
    # print(str(remove_duplicates2(a)))
    # print(str(remDup(a)))
    #
    a = [5,5,5,7,8,8,9]
    # print(str(remove_duplicates2(a)))
    # print(str(remDup(a)))

    print(redDup(a, 2))
