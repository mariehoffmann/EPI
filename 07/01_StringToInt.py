__author__ = 'Marie Hoffmann ozymandiaz147@googlemail.com'


'''
    Convert string representing signed integer to integer without using library functions.
'''

def stringToInt(s):
    n = 0
    if len(s) == 0 or len(s) == 1 and (ord(s[0]) < 48 or ord(s[0]) > 57):
        return n
    sign = -1 if s[0] == '-' else 1
    if s[0] == '-' or s[0] == '+':
        s = s[1:]
    for i in range(len(s)):
        n = 10*n + ord(s[i]) - 48
    return n*sign


print stringToInt('123')
print stringToInt('-123')
print stringToInt('+3678')
print stringToInt('+0')


