__author__ = 'Marie Hoffmann ozymandiaz147@googlemail.com'

import math
import copy


# in:   str word of 64 bits '011001..0'
# out:  bits reversed
def reverseBits(word):
    w = copy.copy(word)
    n = len(word)
    for i in range(int(math.ceil(n/2))):
        w = "".join([w[:i], w[n-i-1], w[i+1:n-i-1], w[i], w[n-i:]])
    return w

# word is integer in [0, 2^{n}-1]
# idea: if binary representation contains 1 at i-th position, add 2^{n-i-1} to new integer
# runtime: O(n), space: O(1) <- ok if needed not too many times or n varying
def reverseBits2_old(word, n):
    x = word
    y = 0
    for i in reversed(list(range(n))):
        if x % math.pow(2, i) < x:
            y += math.pow(2, n-i-1)
            x %= math.pow(2, i)
    return int(y)

def reverseBits2(x, n):
    y = 0
    for i in range(n):
        if x % 2 == 0:
            y += 1 << i
        x >>= 1
    return y

# word is integer in [0, 2^64-1]
# idea: use direct-access lookup table for size-fixed chunks, e.g. length 16
# use shift to get rid of head and tail bits
# runtime O(1), space O(n)
def reverseBits3(word, n):
    # create lookup table (normally done once)
    global lookup
    c = int(n/4) # chunk size
    mask = int(math.pow(2, n)-1)
    chunk1 = (mask & word) >> 3*c
    chunk2 = (mask & word << c) >> 3*c
    chunk3 = (mask & word << 2*c) >> 3*c
    chunk4 = (mask & word << 3*c) >> 3*c
    return lookup[chunk1] + (lookup[chunk2] << c) + (lookup[chunk3] << 2*c) + (lookup[chunk4] << 3*c)


global lookup
chunksize = 2
wordsize = 8
lookup = [0]*int(math.pow(2, chunksize))
#print(str(lookup))
#print(str(list(range(int(math.pow(2,chunksize))))))
for n in list(range(int(math.pow(2,chunksize)))):
    lookup[n] = reverseBits2(n, chunksize)

print(reverseBits3(10, wordsize))




