'''
https://leetcode.com/problems/lru-cache

Design and implement a data structure for Least Recently Used (LRU) cache. It should support the following operations: get and put.



get(key) - Get the value (will always be positive) of the key if the key exists in the cache, otherwise return -1.
put(key, value) - Set or insert the value if the key is not already present. When the cache reached its capacity, it should invalidate the least recently used item before inserting a new item.


Follow up:
Could you do both operations in O(1) time complexity?

Example:

LRUCache cache = new LRUCache( 2 /* capacity */ );

cache.put(1, 1);
cache.put(2, 2);
cache.get(1);       // returns 1
cache.put(3, 3);    // evicts key 2
cache.get(2);       // returns -1 (not found)
cache.put(4, 4);    // evicts key 1
cache.get(1);       // returns -1 (not found)
cache.get(3);       // returns 3
cache.get(4);       // returns 4

'''
class Node:
    def __init__(self, key, value, left, right):
        self.key = key
        self.value = value
        self.left = left
        self.right = right

class LRUCache(object):

    # use deque to construct the cache
    # left/right points are easy to priotize nodes

    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.capacity = capacity
        self.size = 0
        self.lookup = {}
        self.head = Node(-1, -1, None, None)
        self.tail = Node(-1, -1, None, None)

        self.head.right = self.tail
        self.tail.left = self.head


    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        if key not in self.lookup:
            return -1
        else:
            cur = self.lookup.get(key)
            self._prioritize(cur)

            self._print()

            return cur.value

        

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: void
        """

        node = Node(key, value, None, None)
        self.lookup[key] = node
        self._prioritize(node)
        self.size += 1

        if self.size > self.capacity:
            self._evict_last()

        self._print()


    def _evict_last(self):
        evicted_node = self.tail.left

        evicted_node.left.right = self.tail
        self.tail.left = evicted_node.left
        self.lookup.pop(evicted_node.key)
        self.size -= 1
    
    def _prioritize(self, node):
        # print node.left.key, node.key, node.right.key,
        if node.left:
            node.left.right = node.right

        if node.right:
            node.right.left = node.left

        node.right = self.head.right
        self.head.right.left = node
        self.head.right = node
        node.left = self.head

        

    def _print(self):
        pass
        # print self.lookup.keys(),
        # node = self.head
        # while node:
        #     print node.key,
        #     node = node.right
        # print