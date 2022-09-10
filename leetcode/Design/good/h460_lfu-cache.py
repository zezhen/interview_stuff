'''
https://leetcode.com/problems/lfu-cache/description/

Design and implement a data structure for Least Frequently Used (LFU) cache. It should support the following operations: get and put.

get(key) - Get the value (will always be positive) of the key if the key exists in the cache, otherwise return -1.
put(key, value) - Set or insert the value if the key is not already present. When the cache reaches its capacity, it should invalidate the least frequently used item before inserting a new item. For the purpose of this problem, when there is a tie (i.e., two or more keys that have the same frequency), the least recently used key would be evicted.

Follow up:
Could you do both operations in O(1) time complexity?

Example:

LFUCache cache = new LFUCache( 2 /* capacity */ );

cache.put(1, 1);
cache.put(2, 2);
cache.get(1);       // returns 1
cache.put(3, 3);    // evicts key 2
cache.get(2);       // returns -1 (not found)
cache.get(3);       // returns 3.
cache.put(4, 4);    // evicts key 1.
cache.get(1);       // returns -1 (not found)
cache.get(3);       // returns 3
cache.get(4);       // returns 4

'''

class LFUCache(object):

    # 
    # 1. hashmap: key -> (value, FreqDequeNode)
    # 2. hashmap: frequency -> FreqDequeNode
    # 3. Frequency Deque: freq, LruDequeNode, hashmap: keys->LruDequeNode
    # 4. LruDequeNode

    def __init__(self, capacity):
        """
        :type capacity: int
        """

        self.keyCache = {}
        self.freqCache = {}
        self.capacity = capacity
        self.size = 0

        

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        value, node = self.keyCache[key]

        self.updateFreq(key)

        return value


        

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: void
        """

        if key not in self.keyCache:
            self.size += 1
            freqNode = FreqDequeNode()
        else:
            _, freqNode = self.keyCache[key]

        self.keyCache[key] = (value, freqNode)
        self.updateFreq(key)
        if self.size > capacity:
            self.remove()

    def remove(self):
        # head of FreqDequeNode
        # remove first or tail pending on insert implementation



    def updateFreq(self, key):
        lruNode = node.keys.pop(key)
        # todo: lrunode remove itself from list

        freq = node.freq + 1
        newNode = self.freqCache[freq]

        # todo add lruNode into newNode


# Your LFUCache object will be instantiated and called as such:
# obj = LFUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)