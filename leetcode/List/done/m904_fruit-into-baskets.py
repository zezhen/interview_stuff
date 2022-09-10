'''
https://leetcode.com/problems/fruit-into-baskets/description/

In a row of trees, the i-th tree produces fruit with type tree[i].

You start at any tree of your choice, then repeatedly perform the following steps:

Add one piece of fruit from this tree to your baskets.  If you cannot, stop.
Move to the next tree to the right of the current tree.  If there is no tree to the right, stop.
Note that you do not have any choice after the initial choice of starting tree: you must perform step 1, then step 2, then back to step 1, then step 2, and so on until you stop.

You have two baskets, and each basket can carry any quantity of fruit, but you want each basket to only carry one type of fruit each.

What is the total amount of fruit you can collect with this procedure?

 

Example 1:

Input: [1,2,1]
Output: 3
Explanation: We can collect [1,2,1].
Example 2:

Input: [0,1,2,2]
Output: 3
Explanation: We can collect [1,2,2].
If we started at the first tree, we would only collect [0, 1].
Example 3:

Input: [1,2,3,2,2]
Output: 4
Explanation: We can collect [2,3,2,2].
If we started at the first tree, we would only collect [1, 2].
Example 4:

Input: [3,3,3,1,2,1,1,2,3,3,4]
Output: 5
Explanation: We can collect [1,2,1,1,2].
If we started at the first tree or the eighth tree, we would only collect 4 fruits.
 

Note:

1 <= tree.length <= 40000
0 <= tree[i] < tree.length

'''
from collections import Counter
class Solution(object):
    def totalFruit(self, tree):
        """
        :type tree: List[int]
        :rtype: int
        """
        counter = Counter()

        ans = left = 0
        types = 0

        for right, t in enumerate(tree, 1):
            if counter[t] == 0:
                types += 1
            counter[t] += 1

            while types > 2:
                counter[tree[left]] -= 1
                if counter[tree[left]] == 0:
                    types -= 1
                left += 1

            ans = max(ans, right - left)

        return ans

s = Solution()
print s.totalFruit([3,3,3,1,2,1,1,2,3,3,4]) == 5
print s.totalFruit([1,2,3,2,2]) == 4
print s.totalFruit([0,1,2,2]) == 3
print s.totalFruit([1,2,1]) == 3
print s.totalFruit([1,1]) == 2
print s.totalFruit([1]) == 1

