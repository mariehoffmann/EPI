__author__ = 'Marie Hoffmann ozymandiaz147@googlemail.com'

class LinkedList(object):

    class Cell(object):
        def __init__(self, value):
            self.value = value
            self.next = None

    # generate list from array elements
    def __init__(self, A):
        self.head = None
        self.tail = None
        cells = []
        for a in A:
            cells.append(self.Cell(a))
        if len(A) > 0:
            self.head = cells[0]
            self.tail = cells[-1]
            cell_prev = self.head
            for cell in cells[1:]:
                cell_prev.next = cell
                cell_prev = cell
            del cells

    def printCells(self):
        curr = self.head
        output = []
        while curr is not None:
            output.append(str(curr.value) + ' -> ')
            curr = curr.next
        print(''.join(output)[:-4])


# reverse singly linked list with only constant additional memory
def reverseList(L):
    prev = L.head
    curr = prev.next
    L.tail = prev
    L.head = prev
    while curr is not None:
        L.head = curr
        oldNext = curr.next
        curr.next = prev
        prev = curr
        curr = oldNext
    L.tail.next = None
    return L


LL = LinkedList([1,4,6,7,81,99])
print "linked list: "
LL.printCells()

print "reversed: "
L = reverseList(LL)
LL.printCells()