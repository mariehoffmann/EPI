__author__ = 'Marie Hoffmann ozymandiaz147@googlemail.com'

import copy

# return all mnemonics that can be formed given a key map and a number
# ignore unmapped numbers, runtime: O(n*4**n) (max. 4 recursive calls per digit and array copy)
def mnemonics(keymap, number, i=0, aux='', result=[]):
    if i == len(number):
        result.append(aux)
        return
    for letter in keymap.get(number[i], [None]):    # at most 4 letters
        aux1 = copy.copy(aux)                       # O(n)
        aux1 += letter if letter is not None else ''
        mnemonics(keymap, number, i+1, aux1, result)
    return result


keymap = {2: ['A', 'B', 'C'], 3: ['D', 'E', 'F'], 4: ['G', 'H', 'I'], 5: ['J', 'K', 'L'], \
          6: ['M', 'N', 'O'], 7: ['P', 'Q', 'R', 'S'], 8: ['T', 'U', 'V'], 9: ['W', 'X', 'Y', 'Z']}

print(mnemonics(keymap, [2,1,9,0]))