__author__ = 'Marie Hoffmann ozymandiaz147@googlemail.com'

'''
    Translate encodings like 'A', 'AA', 'AD' to integers starting with 1 for 'A'.
'''

# s in {'A', ..., 'Z'}^m
# runtime O(n), space O(1)
def spreadsheet_decoder(s):
    n = 0
    for d in s:
        n = n*26 + ord(d) - ord('A') + 1
    return n

print "'A' decoded is ", spreadsheet_decoder('A')
print "'AA' decoded is ", spreadsheet_decoder('AA')
print "'AD' decoded is ", spreadsheet_decoder('AD')
print "'DEAA' decoded is ", spreadsheet_decoder('DEAA')

