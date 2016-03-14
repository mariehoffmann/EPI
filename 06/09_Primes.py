__author__ = 'Marie Hoffmann ozymandiaz147@googlemail.com'

'''
    Return all primes between 2 and n
'''

import math
import timeit

# idea 1: construct set of multiples of [2,n/2] and intersect with [n]
# runtime: O(n), space: O(n)
def primes(n):
    m = int(math.ceil(n/2))
    S1 = set([l*k for l in list(range(2,m+1)) for k in list(range(2,m+1)) if l*k <= n])
    S2 = set(list(range(2,n+1)))
    P = S2.difference(S1)
    return sorted(list(P))

# idea 2: observation -- non-primes are multiples of primes
# => iterate i in [3..10] and test if current i is multiple of already found primes (which must be less)
# runtime: O(n*p), space: O(p)
def primes2(n):
    P = set([2])
    for i in list(range(3, n+1)):
        if len([1 for p in P if i % p is 0]) is 0:
            P.add(i)
    return sorted(list(P))

# idea 3: use bit array to indicate primes (1) and non-primes (0), iterate from left to right, e.g. p[0] represents 2 and so on
# whenever p_i == 1, cancel prime bit on all positions power(i+2, k) <= n, multiples in between are already covered by previous
# prime multiples/powers! We have to perform p*log(n) such cancellations. Exception is p = 2, optimization: consider only odds
def primes3(n):
    p = [1]*(n-2) # first bit represents 2 and is a known prime
    for i in list(range(int(math.sqrt(n)))):
        if p[i] == 1: # p[i] is prime, cancel out pow(i+2,k)
            j = (i+2)*2
            while j < n:
                p[j-2] = 0
                j += (i+2)
    return [i+2 for i in list(range(n-2)) if p[i] == 1]

# improvement: only odds are candidates, and multiples of p*p need to sieved out, because for p' < p subset of k*p is already
# sieved out
def primes4(n):
    a = [1]*int(math.ceil((n-1)/2))
    for i in range(int(math.ceil((n-1)/2))):
        if a[i] == 1:
            p = (2*i+3)
            j = p*p
            while j <= n:
                a[(j-3)/2] = 0
                j += p
    return [2*a_i+3 for a_i in a if a_i == 1]




def primes5(n):
    # for 3:2:n
    prime_bits = [1]*((n-2) // 2)
    for i in range(len(prime_bits)):
        if prime_bits[i] == 1: # cancel all multiples of prime k*p, with k = p^l
            offset = 2*i+3 # constant
            j = offset*offset # uncompressed offset, compress to use as integer
            print("offset = {:d}, j = {:d}".format(offset, j))
            while (j-3) // 2 < len(prime_bits):
                prime_bits[(j-3) // 2] = 0
                j *= offset

    print
    return [2*i + 3 for i in range(len(prime_bits)) if prime_bits[i] == 1]


if __name__  == "__main__":
    # start = timeit.timeit()
    # primes(10000)
    # end = timeit.timeit()
    # print("primes1.time = " + str(end-start))
    #
    # start = timeit.timeit()
    # primes2(10000)
    # end = timeit.timeit()
    # print("primes2.time = " + str(end-start))
    #
    # start = timeit.timeit()
    # primes3(10000)
    # end = timeit.timeit()
    # print("primes3.time = " + str(end-start))
    #
    # start = timeit.timeit()
    #
    # primes5(10000)
    # end = timeit.timeit()
    # print("primes4.time = " + str(end-start))
    print(str(primes5(10)))


