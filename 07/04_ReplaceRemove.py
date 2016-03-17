__author__ = 'Marie Hoffmann ozymandiaz147@googlemail.com'

# remove 'b', replace 'a' by 'dd' with no additional storage
# s = [c1, ..., cn, None_1, ..., None_n] <- 'allocated' space for string array
def replaceRemove(s):
    n = len(s)//2
    j = -1
    cnt_a = 0 # count 'a's for 2nd step
    # 1st step remove 'b'
    for i in range(n):
        if j > -1 and s[i] != 'b':
            s[j] = s[i]
            j += 1
        if s[i] == 'b' and j < 0:
            j = i
        if s[i] == 'a':
            cnt_a += 1
    if j > -1:
        n = j
        for i in range(j-1, n):
            s[i] = None
    # 2nd step
    if cnt_a > 0:
        for i in reversed(range(n+1)):
            if s[i] != 'a':
                s[i+cnt_a] = s[i]
            else:
                s[i+cnt_a] = 'd'
                cnt_a -= 1
                s[i+cnt_a] = 'd'


    return ''.join(filter(lambda x: x != None, [c for c in s]))

s = 'punk boy'
print(replaceRemove([c for c in s]+[None for _ in range(len(s))]))

s = 'a punk boy had a dream'
print(replaceRemove([c for c in s]+[None for _ in range(len(s))]))

