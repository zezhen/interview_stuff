'''
https://leetcode.com/problems/insert-delete-getrandom-o1-duplicates-allowed/description/

Design a data structure that supports all following operations in average O(1) time.

Note: Duplicate elements are allowed.
insert(val): Inserts an item val to the collection.
remove(val): Removes an item val from the collection if present.
getRandom: Returns a random element from current collection of elements. The probability of each element being returned is linearly related to the number of same value the collection contains.
Example:

// Init an empty collection.
RandomizedCollection collection = new RandomizedCollection();

// Inserts 1 to the collection. Returns true as the collection did not contain 1.
collection.insert(1);

// Inserts another 1 to the collection. Returns false as the collection contained 1. Collection now contains [1,1].
collection.insert(1);

// Inserts 2 to the collection, returns true. Collection now contains [1,1,2].
collection.insert(2);

// getRandom should return 1 with the probability 2/3, and returns 2 with the probability 1/3.
collection.getRandom();

// Removes 1 from the collection, returns true. Collection now contains [1,2].
collection.remove(1);

// getRandom should return 1 and 2 both equally likely.
collection.getRandom();
'''
import collections
import bisect
class RandomizedCollection(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.elements = []
        self.indexs = collections.defaultdict(list)

    def insert(self, val):
        """
        Inserts a value to the collection. Returns true if the collection did not already contain the specified element.
        :type val: int
        :rtype: bool
        """
        exist = (val in self.indexs)
        self.elements.append(val)
        self.indexs[val].append(len(self.elements) - 1)
        return not exist
        

    def remove(self, val):
        """
        Removes a value from the collection. Returns true if the collection contained the specified element.
        :type val: int
        :rtype: bool
        """
        if val not in self.indexs: return False
        pos = self.indexs[val]
        p = pos.pop()
        if not pos:
            self.indexs.pop(val)

        last = self.elements.pop()
        print p, len(self.elements)
        if p != len(self.elements):
            self.elements[p] = last
            self.indexs[last].pop()
            bisect.insort(self.indexs[last], p)
        return True
        

    def getRandom(self):
        """
        Get a random element from the collection.
        :rtype: int
        """
        if not self.elements: return -1
        
        return random.choice(self.elements)
        


# Your RandomizedCollection object will be instantiated and called as such:
# obj = RandomizedCollection()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()