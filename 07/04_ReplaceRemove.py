__author__ = 'Marie Hoffmann ozymandiaz147@googlemail.com'
'''
    Remove 'b', replace 'a' by 'dd' with no additional storage.
    s = [c1, ..., cn, None_1, ..., None_n] <- 'allocated' space for string array
    3 cases: for 'a' write 'dd' into 2nd half, for b nothing, other letters are just copied,
    ptr i points to next element to analyze in 1st half, j to next free slot in 2nd half
'''

# runtime O(n)
def replace_remove(s):
    i = len(s)/2-1
    j = len(s)-1
    while i > -1:
        if s[i] == 'a':
            s[j] = 'd'
            s[j-1] = 'd'
            j -= 2
        elif s[i] != 'b':
            s[j] = s[i]
            j -= 1
        i -= 1
    return ''.join(s[j+1:])


s = 'a punk boy had a dream'
print(replace_remove([c for c in s]+[None for _ in range(len(s))]))

