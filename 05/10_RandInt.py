__author__ = 'Marie Hoffmann ozymandiaz147@googlemail.com'

import random
import math

# binary PRNG
def randBinary():
    return random.randint(0,1)


# return uniformly distributed random int in [a,b]
# idea: each toss path has prob (1/2)**toss
# use binary representation of toss path to represent int in [0, 2**toss-1]
# runtime O(ceil(log(b-a)))
def randInt(a, b):
    toss = int(2**math.ceil(math.log(b-a, 2)))
    path = 0
    i = 0
    while i < toss:
        r = randBinary()
        if r == 1:
            path += 1 << i
        i += 1
        if path > (b-a): # ignore values above (b-a)
            path = 0
            i = 0
    return a + path

n = 1000.
ints = [randInt(2,4) for _ in range(int(n))]
print("freq(2) = " + str(len(filter(lambda i: i == 2, ints))/n))
print("freq(3) = " + str(len(filter(lambda i: i == 3, ints))/n))
print("freq(4) = " + str(len(filter(lambda i: i == 4, ints))/n))


