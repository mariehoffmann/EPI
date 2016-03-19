__author__ = 'Marie Hoffmann ozymandiaz147@googlemail.com'

'''
    Test for palindromicity ignoring non-alphanumeric symbols and cases.
'''

# runtime: O(n), space: O(1)
def is_palindromic(s):
    i, j = 0, len(s)-1
    s = s.upper()
    while i < j:
        while ord(s[i]) < 65 or ord(s[i]) > 90:
            i += 1
        while ord(s[j]) < 65 or ord(s[j]) > 90:
            j -= 1
        if s[i] != s[j]:
            return False
        # else s[i] == s[j] and we forward ptrs
        i += 1
        j -= 1

    return True

print is_palindromic('A man, a plan, a canal, Panama.')
print is_palindromic('Able was I, ere I saw Elba!')
print is_palindromic('Ray a Ray')
print is_palindromic('y')
