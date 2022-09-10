'''
https://leetcode.com/problems/create-maximum-number/description/

Given two arrays of length m and n with digits 0-9 representing two numbers. Create the maximum number of length k <= m + n from digits of the two. The relative order of the digits from the same array must be preserved. Return an array of the k digits.

Note: You should try to optimize your time and space complexity.

Example 1:

Input:
nums1 = [3, 4, 6, 5]
nums2 = [9, 1, 2, 5, 8, 3]
k = 5
Output:
[9, 8, 6, 5, 3]
Example 2:

Input:
nums1 = [6, 7]
nums2 = [6, 0, 4]
k = 5
Output:
[6, 7, 6, 0, 4]
Example 3:

Input:
nums1 = [3, 9]
nums2 = [8, 9]
k = 3
Output:
[9, 8, 9]

'''

class Solution(object):
    def maxNumber(self, nums1, nums2, k):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :type k: int
        :rtype: List[int]
        """

        # the conbination 

        def merge(arr1, arr2):
            ans = []
            i = j = 0
            while i < len(arr1) and j < len(arr2):
                # [6,7] vs [6,0,4]
                if arr1[i] > arr2[j] or arr1[i] == arr2[j] and arr1[i:] > arr2[j:]:
                    ans.append(arr1[i])
                    i += 1
                else: 
                    ans.append(arr2[j])
                    j += 1

            if i < len(arr1): ans.extend(arr1[i:])
            if j < len(arr2): ans.extend(arr2[j:])

            return ans

        def largest(array, k):
            if len(array) <= k: return array
            if k == 0: return []

            ans, stack = [], [array[0]]
            for i in xrange(1, len(array)):
                while stack and array[i] > stack[-1] and len(array) - i + len(stack) > k:
                    stack.pop()
                stack.append(array[i])
            return stack[:k]

        candidate1 = largest(nums1, k)
        candidate2 = largest(nums2, k)

        ans = []
        for i in xrange(min(k, len(nums1))+1):
            j = k - i
            if j > len(nums2): continue

            arr1 = largest(candidate1, i)
            arr2 = largest(candidate2, j)
            ans = max(ans, merge(arr1, arr2))

        return ans


s = Solution()
# print s.maxNumber([],[2], 1) == [2]
# print s.maxNumber([],[1,2], 1) == [2]
# print s.maxNumber([1,2], [], 2) == [1,2]
# print s.maxNumber([], [1,2], 2) == [1,2]
# print s.maxNumber([1],[2], 2) == [2,1]
# print s.maxNumber([1,3,5,7,9],[2,4,6,8], 2) == [9,8]
# print s.maxNumber([1,3,5,7,9],[2,4,6,8], 3) == [9,6,8]
# print s.maxNumber([1,3,5,7,9],[2,4,6,8], 4) == [9,4,6,8]
# print s.maxNumber([1,3,5,7,9],[2,4,6,8], 5) == [9,2,4,6,8]
# print s.maxNumber([1,3,5,7,9],[2,4,6,8], 6) == [8,1,3,5,7,9]
# print s.maxNumber([1,3,5,7,9],[2,4,6,8], 7) == [6,8,1,3,5,7,9]
# print s.maxNumber([3,4,6,5], [9,1,2,5,8,3], 5) == [9,8,6,5,3]
# print s.maxNumber([6,7], [6,0,4], 5) == [6, 7, 6, 0, 4]
# print s.maxNumber([8,6,9], [1,7,5], 3) == [9,7,5]

print s.maxNumber([1,6,5,4,7,3,9,5,3,7,8,4,1,1,4], [4,3,1,3,5,9], 21) == [4, 3, 1, 6, 5, 4, 7, 3, 9, 5, 3, 7, 8, 4, 1, 3, 5, 9, 1, 1, 4]

# print s.maxNumber(range(10000),range(10000), 1000)