'''
https://leetcode.com/problems/all-oone-data-structure/description/

Implement a data structure supporting the following operations:

Inc(Key) - Inserts a new key with value 1. Or increments an existing key by 1. Key is guaranteed to be a non-empty string.
Dec(Key) - If Key's value is 1, remove it from the data structure. Otherwise decrements an existing key by 1. If the key does not exist, this function does nothing. Key is guaranteed to be a non-empty string.
GetMaxKey() - Returns one of the keys with maximal value. If no element exists, return an empty string "".
GetMinKey() - Returns one of the keys with minimal value. If no element exists, return an empty string "".
Challenge: Perform all these in O(1) time complexity.
'''

class DequeNode:
    def __init__(self, count, left, right):
        self.count = count
        self.keys = set()
        self.left = left
        self.right = right

class AllOne(object):

    # hashmap: key -> count
    # list(set): count -> keys set

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.cache = {}

        self.one = DequeNode(1, None, None)
        self.head = self.tail = self.one

    def inc(self, key):
        """
        Inserts a new key <Key> with value 1. Or increments an existing key by 1.
        :type key: str
        :rtype: void
        """
        if key not in self.cache:
            if self.head.count != 1:
                self.head = self.one
            
            self.head.keys.add(key)
            self.cache[key] = self.head
        else:
            node = self.cache[key]

            if len(node.keys) == 1: # contain only one key, modify in-place
                node.count += 1
                return
            
            if node.right == None:
                nextNode = DequeNode(node.count + 1, node, None)
                node.right = nextNode
                self.tail = nextNode
            else:
                nextNode = node.right
                
            node.keys.remove(key)
            nextNode.keys.add(key)
            self.cache[key] = nextNode
            if not self.head.keys:
                self.head = self.head.right
        

    def dec(self, key):
        """
        Decrements an existing key by 1. If Key's value is 1, remove it from the data structure.
        :type key: str
        :rtype: void
        """
        if key not in self.cache: return

        node = self.cache[key]
        if node.count == 1:
            node.keys.remove(key)
            self.cache.pop(key)
            if not self.head.keys and self.head.right:
                self.head = self.head.right
        else:
            count = node.count - 1
            if node.left.count == count:
                newNode = node.left
            else:
                newNode = DequeNode(count, node.left, node)
                node.left.right = newNode
                node.left = newNode

            node.keys.remove(key)
            if len(node.keys) == 0: # empty and remove
                if self.tail == node:
                    self.tail = node.left
                    self.tail.right = None
                else:
                    node.left.right = node.right
                    node.right.left = node.left

            newNode.keys.add(key)
            self.cache[key] = newNode
            if self.head.count > newNode.count:
                self.head = newNode
        

    def getMaxKey(self):
        """
        Returns one of the keys with maximal value.
        :rtype: str
        """
        return next(iter(self.tail.keys)) if self.tail.keys else ''


    def getMinKey(self):
        """
        Returns one of the keys with Minimal value.
        :rtype: str
        """
        return next(iter(self.head.keys)) if self.head.keys else ''


# Your AllOne object will be instantiated and called as such:
obj = AllOne()

obj.inc('a')
assert obj.getMaxKey() == 'a'
assert obj.getMinKey() == 'a'

obj.dec('a')
assert obj.getMaxKey() == ''
assert obj.getMinKey() == ''

obj.inc('a')
obj.inc('a')
assert obj.getMaxKey() == 'a'
assert obj.getMinKey() == 'a'
obj.inc('b')
assert obj.getMaxKey() == 'a'
assert obj.getMinKey() == 'b'

obj.inc('a')
obj.inc('a')
assert obj.getMaxKey() == 'a'

obj.inc('c')
obj.inc('c')
assert obj.getMaxKey() == 'a'
assert obj.getMinKey() == 'b'

obj.dec('a')
obj.dec('a')
assert obj.getMaxKey() == 'a'
assert obj.getMinKey() == 'b'

obj.dec('a')
assert obj.getMaxKey() == 'c'


one = AllOne()
one.inc('a')
one.inc('b')
one.inc('b')
one.inc('c')
one.inc('c')
one.inc('c')
one.dec('b')
one.dec('b')
assert one.getMinKey() == 'a'
one.dec('a')
assert one.getMaxKey() == 'c'
assert one.getMinKey() == 'c'