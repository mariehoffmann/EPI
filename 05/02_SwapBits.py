__author__ = 'Lyssa'

# x & (x-1) clears lowest bit set, x & ~(x-1) extracts lowest bit
# swap x[i] and x[j]
def swapBits(x, i, j):
    bit_i = (x >> i) & 1    #(x&(1<<i)) >> i
    bit_j = (x >> j) & 1    #(x&(1<<j)) >> j
    if bit_i != bit_j:      # or bit_mask = 1L << i | 1 << j, x ^= bit_mask
        if bit_i == 1:
            i, j = j, i
        x += 1 << i
        x -= 1 << j
    return x


print(swapBits(5, 0, 1))
print(swapBits(1, 0, 1))

