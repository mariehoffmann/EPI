__author__ = 'Marie Hoffmann ozymandiaz147@googlemail.com'

# word integer in [0:2^32-1]
def parityBit(word):
    if word == 0:
        return 0
    p = 1
    for i in range(word):
        p = p ^ (word & (1 << i) >> i)
    return p

# O(n)
def parityBits(wordlist):
    return reduce(lambda i,j: i^j, map(parityBit, wordlist), 0)

# O(log(n)), assume word be a pos. integer of 64 bits
# xoring every bit results in 1 if odd, else 0, also true for "partial digestions"
# can be done from left to right or with binary partition scheme
# same effect: reduce(lambda b1, b2: b1^b2, word_2), but linear
def parityBit2(word):
    word ^= word >> 32 # xor first and second half, ignore 1st half
    word ^= word >> 16 # xor 1st and 2nd half of partial digest
    word ^= word >> 8
    word ^= word >> 4
    word ^= word >> 2
    word ^= word >> 1
    return word % 2

if __name__ == "__main__":
    print(parityBit(5))
    print(parityBits([3,3]))
    print(parityBit2(5))
    print(parityBit2(4))

