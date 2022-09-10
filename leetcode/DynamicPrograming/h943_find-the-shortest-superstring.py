'''
https://leetcode.com/problems/find-the-shortest-superstring
https://leetcode.com/articles/find-the-shortest-superstring
Given an array A of strings, find any smallest string that contains each string in A as a substring.

We may assume that no string in A is substring of another string in A.

 


Example 1:


Input: ["alex","loves","leetcode"]
Output: "alexlovesleetcode"
Explanation: All permutations of "alex","loves","leetcode" would also be accepted.



Example 2:


Input: ["catg","ctaagt","gcta","ttca","atgcatc"]
Output: "gctaagttcatgcatc"

 



Note:


	1 <= A.length <= 12
	1 <= A[i].length <= 20



 
'''
import collections
class Solution(object):
    def shortestSuperstring(self, A):
        """
        :type A: List[str]
        :rtype: str
        """
        
        def overlap(a, b):
            i, j = len(a) - 1, 0
            while i >= 0 and j < len(b) and a[i] == b[j]:
                i -= 1
                j += 1
            return j + 1

        indegree = collections.defaultdict(list)
        for i in xrange(len(A)):
            for j in xrange(i+1, len(A)):
                ioj = overlap(A[i], A[j])
                joi = overlap(A[j], A[i])

                indegree[i].append((joi,j))
                indegree[j].append((ioj,i))



        stack = [(start, 0)]
        visited = set([start])
        ans = []
        while stack:
            index, suffix = stack.pop()
            word = A[index]
            # ans.append(word[:len(word)-suffix])
            ans.append(index)
            
            prefixOverlapWords = indegree[index]
            prefixOverlapWords.sort()

            for overlap, i in prefixOverlapWords:
                if i not in visited:
                    stack.append((i, overlap))
                    visited.add(i)

        print ans
        print map(lambda i:A[i], ans)

        # return ''.join(reversed(ans))

s = Solution()
print s.shortestSuperstring(["catg","ctaagt","gcta","ttca","atgcatc"])






