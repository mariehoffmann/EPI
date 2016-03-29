__author__ = 'Marie Hoffmann ozymandiaz147@googlemail.com'

'''
    Write function that tests binary tree property.
'''

import itertools
import operator

class BST(object):

    def __init__(self):
        self.root = None

    def insert(self, key):
        node = self.root
        node_new = Node(key)
        if node is None:
            self.root = node_new
            return
        parent = None
        isLeft = True
        while node is not None:
            parent = node
            if node.key >= key:
                node = node.left
                isLeft = True
            else:
                node = node.right
                isLeft = False
        if isLeft is True:
            parent.left = node_new
        else:
            parent.right = node_new
        node_new.parent = parent

    def print_tree(self):
        queue = [(self.root, 1)]
        while len(queue) > 0:
            item = queue.pop(0)
            print "pos ", item[1], ": ", item[0].key
            if item[0].left is not None:
                queue.append((item[0].left, item[1]*2))
            if item[0].right is not None:
                queue.append((item[0].right, item[1]*2+1))

class Node(object):

    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None


# version 1: inorder traversal generates sorted list if tree has bst property
# runtime O(n), space O(n)
def inorder_traversal(node, acc):
    if node is None:
        return acc
    inorder_traversal(node.left, acc)
    acc.append(node.key)
    inorder_traversal(node.right, acc)
    return acc

def test_bst_property(bst):
    inorder_list = inorder_traversal(bst.root, [])
    pairs = zip(inorder_list, inorder_list[1:])
    return all(itertools.starmap(operator.le, pairs))


# version 2: optimize for nodes of low depth, use bfs with queue and constraint check
# more concrete: on pop test whether nodes key is in permitted range,
#                if true adjust key constraints for children and push
# runtime O(n), space O(n), at most n/2 nodes in queue if BST prop violated on lowest level or not at all
def test_bst_property2(bst):
    inf_int = 2**1000  # assume integer as type(key)
    queue = [(bst.root, [-inf_int, inf_int])]
    while (len(queue) > 0):
        node, limits = queue.pop(0)
        if node.key > limits[0] and node.key < limits[1]:
            if node.left is not None:
                queue.append((node.left, [limits[0], node.key]))
            if node.right is not None:
                queue.append((node.right, [node.key, limits[1]]))
        else:
            return False
    return True


bst = BST()
[bst.insert(i) for i in [4,3,5,8]]
bst.print_tree()
print "has BST property (inorder): ", test_bst_property(bst)
print "has BST property (queue): ", test_bst_property2(bst)


# manipulate keys
bst.root.key = 10
bst.print_tree()
print "has BST property (inorder): ", test_bst_property(bst)
print "has BST property (queue): ", test_bst_property2(bst)

