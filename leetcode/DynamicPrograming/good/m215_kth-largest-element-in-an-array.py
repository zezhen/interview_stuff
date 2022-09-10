'''
https://leetcode.com/problems/kth-largest-element-in-an-array/description/

Find the kth largest element in an unsorted array. Note that it is the kth largest element in the sorted order, not the kth distinct element.

Example 1:

Input: [3,2,1,5,6,4] and k = 2
Output: 5
Example 2:

Input: [3,2,3,1,2,4,5,5,6] and k = 4
Output: 4
Note: 
You may assume k is always valid, 1 <= k <= array's length.
'''

import heapq
class Solution(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        return heapq.nlargest(k, nums)[-1]

    def findKthLargest2(self, nums, k):
        L = len(nums)

        def partition(lo, hi):
            s = random.randint(lo, hi)
            nums[lo], nums[s] = nums[s], nums[lo]
            
            pivot = nums[lo]

            i = lo + 1
            j = hi
            while i <= j:
                while i <= j and nums[i] < pivot:
                    i += 1

                while i <= j and nums[j] >= pivot: # >=
                    j -= 1

                if i <= j:
                    nums[i], nums[j] = nums[j], nums[i]

            nums[j], nums[lo] = nums[lo], nums[j]

            return j


        def helper(lo, hi, k):

            if lo >= hi:
                return nums[lo]

            pivot = partition(lo, hi)
            if pivot  == k:
                return nums[k]

            if pivot > k: # keep in mind this line
                return helper(lo, pivot -1, k)
            else:
                return helper(pivot +1, hi, k-pivot)


        return helper(0,L-1, L -k)


'''
1. heap, maintain k size min heap, scan whole array and go through the heap, get the max number O(nlogk)
2. quick-sort-like algo, random find one polit, partition the array, if polit's index > k, do again in new array from [0:polit], else do again in [polit+1:] for k-polit th number O(nlogn)
3. worest case of #2 will be O(N^2), we can shuffle array first to guarantee O(N)

'''