'''
https://leetcode.com/problems/sum-of-subarray-minimums
https://leetcode.com/articles/sum-of-subarray-minimums
Given an array of integers A, find the sum of min(B), where B ranges over every (contiguous) subarray of A.

Since the answer may be large, return the answer modulo 10^9 + 7.

 

Example 1:


Input: [3,1,2,4]
Output: 17
Explanation: Subarrays are [3], [1], [2], [4], [3,1], [1,2], [2,4], [3,1,2], [1,2,4], [3,1,2,4]. 
Minimums are 3, 1, 2, 4, 1, 1, 2, 1, 1, 1.  Sum is 17.

 

Note:


	1 <= A.length <= 30000
	1 <= A[i] <= 30000



 

'''
import bisect

class Solution(object):
    def sumSubarrayMins(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        
        ans, modulo = 0, (10**9 + 7)
        
        # maintain two queues:
        # qvalue: keep the increasing values represent before the min values before now
        # qcount: keep the count of corresponding index in qvalue, and the accumulate value by now.
        # qlen: to guarantee no pop out operation
        # e.g. [3,1,2,4,2,1] the output of index, qvalue, qcount, qlen as below
        # 0 [3] [(1, 3)] 1
        # 1 [1] [(2, 2)] 1
        # 2 [1, 2] [(2, 2), (3, 4)] 2
        # 3 [1, 2, 4] [(2, 2), (3, 4), (4, 8)] 3
        # 4 [1, 2, 4] [(2, 2), (5, 8), (4, 8)] 2
        # 5 [1, 2, 4] [(6, 6), (5, 8), (4, 8)] 1
        qvalue, qcount, qlen = [], [], 0
        
        for i in range(len(A)):
            a = A[i]
            index = bisect.bisect_left(qvalue, a, 0, qlen)
            if index < qlen:
                ci, sumi = qcount[index - 1] if index > 0 else (0, 0) 
                cq, sumq = qcount[qlen-1]
                self.insert(qcount, index, (cq+1, sumi + (cq-ci+1) * a))
                self.insert(qvalue, index, a)
                ans = (ans + sumi + (cq-ci+1) * a) % modulo
            else:
                ci, sumi = qcount[index - 1] if index > 0 else (0, 0)
                self.insert(qcount, index, (ci+1, sumi + a))
                self.insert(qvalue, index, a)
                ans = (ans + (sumi + a)) % modulo
            qlen = index + 1

        return ans
    
    def insert(self, queue, index, value):
        if index < len(queue):
            queue[index] = value
        else:
            queue.append(value)