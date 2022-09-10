'''
https://leetcode.com/problems/find-minimum-in-rotated-sorted-array-ii/description/

Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand.

(i.e.,  [0,1,2,4,5,6,7] might become  [4,5,6,7,0,1,2]).

Find the minimum element.

The array may contain duplicates.

Example 1:

Input: [1,3,5]
Output: 1
Example 2:

Input: [2,2,2,0,1]
Output: 0
Note:

This is a follow up problem to Find Minimum in Rotated Sorted Array.
Would allow duplicates affect the run-time complexity? How and why?
'''

class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        


# copied c++ solution
# class Solution {
# public:
#     int findMin(vector<int> &num) {
#         int lo = 0;
#         int hi = num.size() - 1;
#         int mid = 0;
        
#         while(lo < hi) {
#             mid = lo + (hi - lo) / 2;
            
#             if (num[mid] > num[hi]) {
#                 lo = mid + 1;
#             }
#             else if (num[mid] < num[hi]) {
#                 hi = mid;
#             }
#             else { // when num[mid] and num[hi] are same
#                 hi--;
#             }
#         }
#         return num[lo];
#     }
# };        