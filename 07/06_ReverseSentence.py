__author__ = 'Marie Hoffmann ozymandiaz147@googlemail.com'


'''
    Write Function reversing the sentence, i.e. reverse the ordering of the words.
'''

# idea: reverse string on character level, then reverse words
# Python strings do not support single character assignment
def reverse_sentence(s):
    s = list(s)
    suffix = ''
    if ord(s[-1]) < ord('A') or ord(s[-1]) > ord('z'):
        suffix = s[-1]
        s = s[:-1]
    for i in range(len(s)/2):
        s[i], s[len(s)-i-1] = s[len(s)-i-1], s[i]
    s += [' ']
    i, j = 0, next((i for i, x in enumerate(s) if x == ' '), -1)
    while j > -1:
        for k in range((j-i)/2):
            s[i+k], s[j-1-k] = s[j-1-k], s[i+k]
        i, j = j+1, next((i for i, x in enumerate(s[j+1:], start=j+1) if x == ' '), -1)
    return ''.join(s[:-1]+[suffix])

print reverse_sentence('Alice likes Bob.')
print reverse_sentence('Fatamogana!')
print reverse_sentence('Somewhere else')


