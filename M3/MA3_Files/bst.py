""" bst.py

Student: Oliver Groth
Mail: Oliver.Groth.7974@student.uu.se
Reviewed by: Kieran
Date reviewed: 16 May
"""


from linked_list import LinkedList
import random
import matplotlib.pyplot as plt
import math


class BST:

    class Node:
        def __init__(self, key, left=None, right=None):
            self.key = key
            self.left = left
            self.right = right

        def __iter__(self):     # Discussed in the text on generators
            if self.left:
                yield from self.left
            yield self.key
            if self.right:
                yield from self.right

    def __init__(self, root=None):
        self.root = root

    def __iter__(self):         # Dicussed in the text on generators
        if self.root:
            yield from self.root

    def insert(self, key):
        self.root = self._insert(self.root, key)

    def _insert(self, r, key):
        if r is None:
            return self.Node(key)
        elif key < r.key:
            r.left = self._insert(r.left, key)
        elif key > r.key:
            r.right = self._insert(r.right, key)
        else:
            pass  # Already there
        return r

    def print(self):
        self._print(self.root)

    def _print(self, r):
        if r:
            self._print(r.left)
            print(r.key, end=' ')
            self._print(r.right)

    def contains(self, k):
        n = self.root
        while n and n.key != k:
            if k < n.key:
                n = n.left
            else:
                n = n.right
        return n is not None

    def size(self):
        return self._size(self.root)

    def _size(self, r):
        if r is None:
            return 0
        else:
            return 1 + self._size(r.left) + self._size(r.right)

#
#   Methods to be completed
#

    def height(self):                             # Compulsory
        return self._height(self.root)

    def _height(self,n):
        if n is None: # Tomt träd höjd 0
            return 0
        hleft = self._height(n.left)
        hright = self._height(n.right)

        return max(hleft,hright) + 1

    def minval(self): # metod för att underlätta remove
        return self._minval(self.root)

    def _minval(self,r):
        while r.left is not None:
            r = r.left
        return r.key

    def remove(self, key):
        self.root = self._remove(self.root, key)

    def _remove(self, r, k):                      # Compulsory
        if r is None:
            return None
        elif k < r.key:
            r.left = self._remove(r.left,k)
        elif k > r.key:
             r.right =  self._remove(r.right,k)
        else:  # This is the key to be removed
            if r.left is None:     # Easy case
                return r.right
            elif r.right is None:  # Also easy case
                return r.left
            else:
                # This is the tricky case.
                # Find the smallest key in the right subtree
                smallkey = self._minval(r.right)
                # Put that key in this node
                r.key = smallkey
                # Remove that key from the right subtree
                r.right = self._remove(r.right,smallkey)
        return r  # Remember this! It applies to some of the cases above

    def __str__(self):                            # Compulsory
        if self.root is None:
            return "<>"
        result = "<"
        for data in self:
            result = result + str(data) + ", "
        result = result[:-2]
        result = result + ">"
        return result

    def to_list(self):                            # Compulsory
        result = []
        if self.root is None:
            return result
        for data in self:
            result = result + [data]
        return result


    def to_LinkedList(self):                      # Compulsory
        result = LinkedList()
        for data in self:
            result.insert(data)
        return result

    def ipl(self):                                # Compulsory
        return self._ipl(self.root, 1)
        
        
    def _ipl(self, r, d):
        if r is None:
            return 0
        # basfall
        if r.left is None and r.right is None:
            return d
        # rekursion
        else:
            return d + self._ipl(r.left,d+1) + self._ipl(r.right,d+1)


def random_tree(n):                               # Useful
    t = BST()
    for i in range(n):
        t.insert(random.random())
    return t


def main():
    #t = BST()
    #for x in [10, 5, 3, 8, 1, 4, 6, 9, 2, 7]:#[4, 1, 3, 6, 7, 1, 1, 5, 8, 0]:
    #    t.insert(x)
    #t.print()
    #print()

    #print('size  : ', t.size())
    #for k in [0, 1, 2, 5, 9]:
    #    print(f"contains({k}): {t.contains(k)}")
    #print(t.height())
    #print(t.minval())
    #t.remove(2)
    #t.remove(1)
    #t.print()
    #print(str(t))
    #t.ipl()

    # övning 20

    #skapar lista med träd
    trees = []
    height = []
    ANH = []
    for n in range(1,100):
        t = random_tree(n)
        h = t.height()
        trees.append(t)
        height.append(h)
        ANH.append(t.ipl() / n)

    print(height)
    print(ANH)
    x = range(1,100)
    # Showing data
    plt.plot(x, ANH)
    # Showing theory
    y = []
    for j in x:
        y.append(1.39*math.log2(j))

    plt.plot(x, y)
    plt.show()

    plt.plot(x,height)
    plt.show()



if __name__ == "__main__":
    main()


"""
What is the generator good for?
==============================
# Förstod det som att generatorn bara itererar genom alla noder i storleksordning


1. computing size? Ja
2. computing height? Nej
3. contains? Ja, men blir långsammare än att söka på tidigare vis
4. insert? Nej
5. remove? Nej




Results for ipl of random trees
===============================






"""
