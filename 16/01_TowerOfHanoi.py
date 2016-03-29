__author__ = 'Marie Hoffmann ozymandiaz147@googlemail.com'

action = "\tmv disc from P{} to P{}"

# idea: utilize solutions for n-1 to (a) build tower on auxiliary pin, (b) mv largest disc to target pin,
# (c) use again solution for n-1 to build tower on target pin on top of largest disc

def tower_hanoi(n, p_from, p_to):
    p_aux = set([1,2,3]).difference(set([p_from, p_to])).pop()
    if n == 1:
        print action.format(p_from, p_to)
        return
    elif n == 2:
        print action.format(p_from, p_aux)
        print action.format(p_from, p_to)
        print action.format(p_aux, p_to)
        return
    else:
        tower_hanoi(n-1, p_from, p_aux)
        print action.format(p_from, p_to)
        tower_hanoi(n-1, p_aux, p_to)

print "How to move 1 disc from P1 to P2:"
tower_hanoi(1, 1, 2)

print "How to move 2 discs from P1 to P2:"
tower_hanoi(2, 1, 2)

print "How to move 3 discs from P1 to P2:"
tower_hanoi(3, 1, 2)

print "How to move 4 discs from P1 to P2:"
tower_hanoi(4, 1, 2)


