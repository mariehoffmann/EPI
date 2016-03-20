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


# inorder traversal generates sorted list if tree has bst property
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


bst = BST()
[bst.insert(i) for i in [4,3,5,8]]
bst.print_tree()
print test_bst_property(bst)

# manipulate keys
bst.root.key = 10
bst.print_tree()
print test_bst_property(bst)


