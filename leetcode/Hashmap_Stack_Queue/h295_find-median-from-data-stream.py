'''
https://leetcode.com/problems/find-median-from-data-stream
https://leetcode.com/articles/find-median-from-data-stream
Median is the middle value in an ordered integer list. If the size of the list is even, there is no middle value. So the median is the mean of the two middle value.
For example,

[2,3,4], the median is 3

[2,3], the median is (2 + 3) / 2 = 2.5

Design a data structure that supports the following two operations:


	void addNum(int num) - Add a integer number from the data stream to the data structure.
	double findMedian() - Return the median of all elements so far.


 

Example:


addNum(1)
addNum(2)
findMedian() -> 1.5
addNum(3) 
findMedian() -> 2


 

Follow up:


	If all integer numbers from the stream are between 0 and 100, how would you optimize it?
	If 99% of all integer numbers from the stream are between 0 and 100, how would you optimize it?

'''
import heapq
class MedianFinder(object):

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.left_heap = []
        self.right_heap = []
        self.median = None

    def addNum(self, num):
        """
        :type num: int
        :rtype: void
        """

        if self.median == None:
            # add the first number
            if not self.left_heap:
                self.median = num
                return

            left_max = - heapq.nsmallest(1, self.left_heap)[0]
            right_min = heapq.nsmallest(1, self.right_heap)[0]

            if num <= left_max:
                self.median = - heapq.heappop(self.left_heap)
                heapq.heappush(self.left_heap, - num)
            elif num >= right_min:
                self.median = heapq.heappop(self.right_heap)
                heapq.heappush(self.right_heap, num)
            else:
                self.median = num
        else:
            if num >= self.median:
                heapq.heappush(self.right_heap, num)
                heapq.heappush(self.left_heap, - self.median)
            else:
                heapq.heappush(self.right_heap, self.median)
                heapq.heappush(self.left_heap, - num)
            self.median = None
        

    def findMedian(self):
        """
        :rtype: float
        """
        if self.median != None:
            return self.median
        else:
            left = - heapq.nsmallest(1, self.left_heap)[0]
            right = heapq.nsmallest(1, self.right_heap)[0]
            return (left + right) / 2.0


finder = MedianFinder()

numbers = [6, 6.0, 10, 8.0, 2, 6.0, 6, 6.0, 5, 6.0, 0, 5.5, 6, 6.0, 3, 5.5, 1, 5.0, 0, 4.0, 0, 3.0]
for i, action in enumerate(["addNum","findMedian","addNum","findMedian","addNum","findMedian","addNum","findMedian","addNum","findMedian","addNum","findMedian","addNum","findMedian","addNum","findMedian","addNum","findMedian","addNum","findMedian","addNum","findMedian"]):
    if action == 'addNum':
        finder.addNum(numbers[i])
    else:
        assert finder.findMedian() == numbers[i]

obj = MedianFinder()
obj.addNum(1)
assert obj.findMedian() == 1.0
obj.addNum(2)
assert obj.findMedian() == 1.5
obj.addNum(3)
assert obj.findMedian() == 2
obj.addNum(4)
assert obj.findMedian() == 2.5
obj.addNum(5)
assert obj.findMedian() == 3

# a = [6,10,2,6,5,0,6,3,1,0,0]
# b = [6.0,8.0,6.0,6.0,6.0,5.5,6.0,5.5,5.0,4.0,3.0]
# assert len(a) == len(b)
# res = [0] * (2*len(a))
# res[0::2] = a
# res[1::2] = b
# print res


class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class MedianFinder_unordered(object):

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.median = None
        self.tail = None
        self.odd = False

    def addNum(self, num):
        """
        :type num: int
        :rtype: void
        """
        
        if self.tail == None:
            n = Node(num)
            self.tail = n
            self.median = n
        else:
            if self.odd:
                n = Node(num)
                self.tail.next = n
            else:
                # median need to move forward, 
                # reuse this node for num
                n = self.median
                self.median = n.next
                n.value = num
                # n.next = None
                self.tail.next = n
            self.tail = n

        self.odd = not self.odd

    def findMedian(self):
        """
        :rtype: float
        """
        if not self.median: return None

        if self.odd:
            return self.median.value * 1.0
        else:
            return (self.median.value + self.median.next.value) / 2.0


# Your MedianFinder object will be instantiated and called as such:
obj = MedianFinder_unordered()
obj.addNum(1)
assert obj.findMedian() == 1.0
obj.addNum(2)
assert obj.findMedian() == 1.5
obj.addNum(3)
assert obj.findMedian() == 2
obj.addNum(4)
assert obj.findMedian() == 2.5
obj.addNum(5)
assert obj.findMedian() == 3

'''
follow up questions:

1. If all integer numbers from the stream are between 0 and 100, how would you optimize it?

create a array with size 101 to keep counter for [0, 100], maintain median_index and offset

median_index is to indicate the position of median in array
offset is to indicate the position of median in cell, considering the counter in cell is greater than 1
if offset > 0, then array[median_index] is the median, if offset is 0, then median = (array[median_index] + array[median_index-1]) / 2

considering there will be some blank cell, to avoid scan froward and backward too many times, we can use deque to keep the counter, use map to keep i -> deque node for quick update.


2. If 99% of all integer numbers from the stream are between 0 and 100, how would you optimize it?

we need to maintain the list structure in follow up #1 and left_heap/right_heap at same time.

left_heap, list, right_heap

if the median fall into the heap in two side, the problem fall back to the scenario at beginning.

'''