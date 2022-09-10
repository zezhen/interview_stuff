'''
https://leetcode.com/problems/top-k-frequent-words
https://leetcode.com/articles/top-k-frequent-words
Given a non-empty list of words, return the k most frequent elements.
Your answer should be sorted by frequency from highest to lowest. If two words have the same frequency, then the word with the lower alphabetical order comes first.

Example 1:

Input: ["i", "love", "leetcode", "i", "love", "coding"], k = 2
Output: ["i", "love"]
Explanation: "i" and "love" are the two most frequent words.
    Note that "i" comes before "love" due to a lower alphabetical order.



Example 2:

Input: ["the", "day", "is", "sunny", "the", "the", "the", "sunny", "is", "is"], k = 4
Output: ["the", "is", "sunny", "day"]
Explanation: "the", "is", "sunny" and "day" are the four most frequent words,
    with the number of occurrence being 4, 3, 2 and 1 respectively.



Note:

You may assume k is always valid, 1 <= k <= number of unique elements.
Input words contain only lowercase letters.



Follow up:

Try to solve it in O(n log k) time and O(n) extra space.

'''

import heapq
class Solution(object):
    def topKFrequent(self, words, k):
        """
        :type words: List[str]
        :type k: int
        :rtype: List[str]
        """
        cache = {}
        for word in words:
            if word not in cache: 
                cache[word] = 0
            cache[word] += 1
        
        queue = []
        for w,c in cache.iteritems():
            heapq.heappush(queue, (-c, w))
                
        return [heapq.heappop(queue)[1] for i in xrange(k)]