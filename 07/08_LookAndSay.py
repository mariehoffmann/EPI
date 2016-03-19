__author__ = 'Marie Hoffmann ozymandiaz147@googlemail.com'


class LinkedList(object):
    class Node(object):
        def __init__(self, digit=None, ctr=None):
            self.digit = digit  # represents digit
            self.ctr = ctr  # group size, i.e. #digits
            self.succ = None

        # insert node after this
        def insert(self, node):
            tmp = self.succ
            self.succ = node
            node.succ = tmp

    def __init__(self, digit=None, ctr=None):
        self.head = self.Node(digit, ctr)

    # merge nodes representing same group
    def merge(self):
        curr = self.head
        #print("curr in merge " +str(curr.digit) + ": " + str(curr.ctr))
        while curr.succ is not None:
            if curr.succ.digit == curr.digit:
                curr.ctr += curr.succ.ctr
                curr.succ = curr.succ.succ
            else:
                curr = curr.succ
        print(self.output())

    # split key and value into new nodes
    def split(self):
        curr = self.head
        while curr is not None:
            curr.insert(self.Node(curr.digit, 1))
            curr.digit = curr.ctr
            curr.ctr = 1
            curr = curr.succ.succ
            print(self.output())

    # applied after merge
    def output(self):
        s = ''
        curr = self.head
        while curr is not None:
            s += str(curr.ctr) + str(curr.digit)
            curr = curr.succ
        return s



# init s = '1', read off digits from left to right and group subsequent digits with same value '#d|d'
# new string is concatenation of group summary, i.e. 1, 11, 21, 1211, 111221, 312211
# runtime O(n2^n), space O(n)
def look_and_say(n):
    s = '1'
    for i in range(1,n):
        s_new = ''
        ctr = 1
        for j in range(1,len(s)):
            if s[j-1] == s[j]:
                ctr += 1
            else:  # digit change: add summary of previous group
                s_new += str(ctr) + s[j-1]
                ctr = 1
        s_new += str(ctr) + s[-1]
        s = s_new
    return s

# different view: manage groups in linked list
# two step algorithm:
#   (i)     summarize (and split), i.e. rewrite group as #d | d and split if #d contains different digits,
#           after this operation nodes represent a single digit
#   (ii) merge neighbouring groups representing same digit
def look_and_say2(n, s = '1'):
    ll = LinkedList(1,1)
    for i in range(n-1):
        # split ctr and digit
        ll.split()
        # merge groups
        ll.merge()
    return ll.output()



if __name__ == "__main__":
    for i in range(8):
        print(look_and_say(i))
        print(look_and_say2(i))


