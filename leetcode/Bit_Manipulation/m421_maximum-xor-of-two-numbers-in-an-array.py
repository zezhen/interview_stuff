'''
https://leetcode.com/problems/maximum-xor-of-two-numbers-in-an-array

Given a non-empty array of numbers, a0, a1, a2, ... , an-1, where 0 <= ai < 231.

Find the maximum result of ai XOR aj, where 0 <= i, j < n.

Could you do this in O(n) runtime?

Example:

Input: [3, 10, 5, 25, 2, 8]

Output: 28

Explanation: The maximum result is 5 ^ 25 = 28.

'''

class Solution(object):
    def findMaximumXOR(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        ans = mask = 0
        for i in xrange(31, -1, -1): # start from significant bits
            mask |= (1 << i)
            andSet = set()
            for num in nums:
                andSet.add(mask & num) # bit i only has two possibilities, 0 or 1.
            tmp = ans | (1 << i)
            for prefix in andSet:
                if (tmp ^ prefix) in andSet:    # tmp ^ prefix in andSet means there are two numbers has 0 or 1 in bit i
                    ans = tmp
                    break
        return ans



# public class Solution {
#     public int findMaximumXOR(int[] nums) {
#         int max = 0, mask = 0;
#         for(int i = 31; i >= 0; i--){
#             mask = mask | (1 << i);
#             Set<Integer> set = new HashSet<>();
#             for(int num : nums){
#                 set.add(num & mask);
#             }
#             int tmp = max | (1 << i);
#             for(int prefix : set){
#                 if(set.contains(tmp ^ prefix)) {
#                     max = tmp;
#                     break;
#                 }
#             }
#         }
#         return max;
#     }
# }

# I think most people who find it hard to understand the code is stuck on this line if(set.contains(tmp ^ prefix))
# The tricky part here is that we need to be aware of a key property of XOR applying on the above line: if A ^ B = C, then A ^ B ^ B = C ^ B, then A = C ^ B
# Before executing that line, max stands for the maximum we can get if we consider only the most significant i - 1 bits, tmp stands for the potential max value we can get when considering the most significant i bits. How can we get this tmp? The only way we can get this value is that we have two values A and B in the set (a set of most significant i bits of each member), such that A ^ B equals to tmp. As mentioned earlier, A ^ B = tmp is equivalent to A = tmp ^ B. Here is where that line comes in: set.contains(tmp ^ B).

# BTW, though this is a great solution, it is actually faulty if the input contains negative numbers (though not required by the problem itself) as i starts from 31 instead of 30. It would be a perfect solution if the input is unsigned int instead.