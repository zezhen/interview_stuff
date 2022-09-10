'''
https://leetcode.com/problems/split-array-into-consecutive-subsequences
https://leetcode.com/articles/split-array-into-consecutive-subsequences
You are given an integer array sorted in ascappendFreqing order (may contain duplicates), you need to split them into several subsequences, where each subsequences consist of at least 3 consecutive integers. Return whether you can make such a split.

Example 1:

Input: [1,2,3,3,4,5]
Output: True
Explanation:
You can split them into two consecutive subsequences : 
1, 2, 3
3, 4, 5



Example 2:

Input: [1,2,3,3,4,4,5,5]
Output: True
Explanation:
You can split them into two consecutive subsequences : 
1, 2, 3, 4, 5
3, 4, 5



Example 3:

Input: [1,2,3,4,4,5]
Output: False



Note:

The length of the input is in range of [1, 10000]

'''
class Solution(object):
    def isPossible(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        # 1. We iterate through the array once to get the frequency of all the elements in the array
        # 2. We iterate through the array once more and for each element we either see if it can be appended to a previously constructed consecutive sequence or if it can be the start of a new consecutive sequence. If neither are true, then we return false.

        freq = collections.Counter(nums)
        appendFreq = collections.Counter()
        for i in nums:
            if not freq[i]: continue
            
            if appendFreq[i] > 0:   # number i can be appened to a previous sequence, see tips1
                appendFreq[i] -= 1
                appendFreq[i+1] += 1    # next candidate
            elif freq[i + 1] and freq[i + 2]:   # construct a new sequence start from i
                freq[i + 1] -= 1
                freq[i + 2] -= 1
                appendFreq[i + 3] += 1  # next candidate
            else:
                return False
            freq[i] -= 1

        return True

# tip1: if number i can be appended to a previous sequence, we do it immediately/greedily, because if i can be a start of a new sequence, we could connect this two sequence to be a longer one, like 1,2,3,4,5,6, while 4 must be a begin of a new sequence, we definitely has multiple 4, like 1,2,3,4,4,5,6, for the first 4, we still can do append.
            


                    



