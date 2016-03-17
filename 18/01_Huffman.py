__author__ = 'Marie Hoffmann ozymandiaz147@googlemail.com'

'''
    Find code book with smallest average code length.
'''

import heapq
import math

ECF = {
'A':    8.167, \
'B':    1.492,\
'C':	2.782,\
'D':	4.253,\
'E':	12.702,\
'F': 	2.228,\
'G': 	2.015,\
'H': 	6.094,\
'I': 	6.966,\
'J': 	0.153,\
'K': 	0.772,\
'L': 	4.025,\
'M': 	2.406,\
'N': 	6.749,\
'O': 	7.507,\
'P': 	1.929,\
'Q': 	0.095,\
'R': 	5.987,\
'S': 	6.327,\
'T': 	9.056,\
'U': 	2.758,\
'V': 	0.978,\
'W': 	2.360,\
'X': 	0.150,\
'Y': 	1.974,\
'Z': 	0.074}

# Huffman code generation algorithm from book: merge nodes with smallest frequencies (sum of subtree frequencies)
# until all subtrees are merged and form a single tree, use priority queue for minimum extraction
# runtime: O(nlogn), space: O(n)
class Node(object):
    def __init__(self, key=None, left=None, right=None):
        self.left = left
        self.right = right
        self.key = key      # key = None, node is inner node else leaf
        self.parent = None
        self.code = ''

def optHuffmanCode(freq):
    h = []
    [heapq.heappush(h, (item[1], Node(item[0]))) for item in freq.items()]  # nlogn
    while len(h) > 1:  # O(n)
        min1 = heapq.heappop(h)  # O(1)
        min2 = heapq.heappop(h)
        node = Node(None, min1[1], min2[1])
        min1[1].parent, min2[1].parent = node, node
        min1[1].code, min2[1].code = '0' + min1[1].code, '1' + min2[1].code
        heapq.heappush(h, (min1[0] + min2[0], node))  # logn
    # traverse tree for building codes
    s = set([heapq.heappop(h)[1]])  # add root
    codes = []
    while len(s) > 0:  # O(n)
        node = s.pop()  # O(1) hash, same for add()
        if node.key != None:
            codes.append((node.key, node.code))
        else: # prepend current node's code
            if node.left != None:
                node.left.code = node.code + node.left.code
                s.add(node.left)
            if node.right != None:
                node.right.code = node.code + node.right.code
                s.add(node.right)
    return codes

# test whether no code is prefix of another
def prefixTest(codes):
    codes.sort(key=lambda x: x[1])
    for i, code in enumerate(codes):
        for code2 in codes[i+1:]:
            if code[1] == code2[1][:len(code[1])]:
                print "Warning: unvalid Huffman code for ", code, " and ", code2



#print optHuffmanCode({'A': .25, 'B': .25, 'C': .25, 'D': .25})
#print optHuffmanCode({'A': .99, 'B': .01/3, 'C': .01/3, 'D': .01/3})

codes = optHuffmanCode(ECF)
prefixTest(codes)
print "Avg Huffman code lengths with priority queue: ", sum([ECF[code[0]]*float(len(code[1])) for code in codes])/100
print "Codes: ", codes

