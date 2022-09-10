'''
https://leetcode.com/problems/increasing-subsequences

Given an integer array, your task is to find all the different possible increasing subsequences of the given array, and the length of an increasing subsequence should be at least 2 .


Example:

Input: [4, 6, 7, 7]
Output: [[4, 6], [4, 7], [4, 6, 7], [4, 6, 7, 7], [6, 7], [6, 7, 7], [7,7], [4,7,7]]



Note:

The length of the given array will not exceed 15.
The range of integer in the given array is [-100,100].
The given array may contain duplicates, and two equal integers should also be considered as a special case of increasing sequence.

'''
from collections import deque
class Solution(object):
    def findSubsequences(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        
        # BFS, keep all candidates increasing sequences in result (length one and more)
        # how to handle the duplicated sequences?
        # 1. convert list to tuple (python)
        # 2. trie?
        # 3. basic?

        ans = []

        def dfs(queue, start):
            if len(queue) >= 2:
                ans.append(list(queue))

            used = set()
            for i in xrange(start, len(nums)):
                if nums[i] in used: continue
                if not queue or nums[i] >= queue[-1]:
                    queue.append(nums[i])
                    used.add(nums[i])
                    dfs(queue, i+1)
                    queue.pop()
        dfs(deque(), 0)
        return ans
        

    def findSubsequences0(self, nums):
        # credit to https://leetcode.com/problems/increasing-subsequences/discuss/97127
        subs = {()}
        for num in nums:
            subs |= {sub + (num,)
                     for sub in subs
                     if not sub or sub[-1] <= num}
        return [list(sub) for sub in subs if len(sub) >= 2]


s = Solution()
nums = [4,3,2,1]
print sorted(s.findSubsequences(nums)) == sorted(s.findSubsequences0(nums))


# public class Solution {
#     public List<List<Integer>> findSubsequences(int[] nums) {
#         List<List<Integer>> res = new LinkedList<>();
#         helper(new LinkedList<Integer>(), 0, nums, res);
#         return res; 
#     }
#     private void helper(LinkedList<Integer> list, int index, int[] nums, List<List<Integer>> res){
#         if(list.size()>1) res.add(new LinkedList<Integer>(list));
#         Set<Integer> used = new HashSet<>();
#         for(int i = index; i<nums.length; i++){
#             if(used.contains(nums[i])) continue;
#             if(list.size()==0 || nums[i]>=list.peekLast()){
#                 used.add(nums[i]);
#                 list.add(nums[i]); 
#                 helper(list, i+1, nums, res);
#                 list.remove(list.size()-1);
#             }
#         }
#     }
# }