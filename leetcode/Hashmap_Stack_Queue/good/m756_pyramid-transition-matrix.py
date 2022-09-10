'''
https://leetcode.com/problems/pyramid-transition-matrix
https://leetcode.com/articles/pyramid-transition-matrix

We are stacking blocks to form a pyramid.  Each block has a color which is a one letter string, like `'Z'`.

For every block of color `C` we place not in the bottom row, we are placing it on top of a left block of color `A` and right block of color `B`.  We are allowed to place the block there only if `(A, B, C)` is an allowed triple.

We start with a bottom row of bottom, represented as a single string.  We also start with a list of allowed triples allowed.  Each allowed triple is represented as a string of length 3.

Return true if we can build the pyramid all the way to the top, otherwise false.


Example 1:

Input: bottom = "XYZ", allowed = ["XYD", "YZE", "DEA", "FFF"]
Output: true
Explanation:
We can stack the pyramid like this:
    A
   / \
  D   E
 / \ / \
X   Y   Z

This works because ('X', 'Y', 'D'), ('Y', 'Z', 'E'), and ('D', 'E', 'A') are allowed triples.



Example 2:

Input: bottom = "XXYX", allowed = ["XXX", "XXY", "XYX", "XYY", "YXZ"]
Output: false
Explanation:
We can't stack the pyramid to the top.
Note that there could be allowed triples (A, B, C) and (A, B, D) with C != D.



Note:

bottom will be a string with length in range [2, 8].
allowed will have length in range [0, 200].
Letters in all strings will be chosen from the set {'A', 'B', 'C', 'D', 'E', 'F', 'G'}.

'''
import collections
class Solution(object):
    def pyramidTransition(self, bottom, allowed):
        """
        :type bottom: str
        :type allowed: List[str]
        :rtype: bool
        """

        cache = collections.defaultdict(list)
        for triple in allowed:
            cache[triple[:2]].append(triple[-1])


        def dfs(_bottom):
            if len(_bottom) == 1: return True

            uplevels = collections.deque()
            for i in xrange(1, len(_bottom)):
                prefix = _bottom[i-1:i+1]
                if prefix not in cache: return False

                if uplevels:
                    size = len(uplevels)
                    while size > 0:
                        cur = uplevels.popleft()
                        for top in cache[prefix]:
                            uplevels.append(cur + top)
                        size -= 1
                else:
                    for top in cache[prefix]:
                        uplevels.append(top)

            while uplevels:
                new_bottom = uplevels.popleft()
                if dfs(new_bottom):
                    return True

            return False

        return dfs(bottom)


s = Solution()
print s.pyramidTransition("XYZ", ["XYD", "YZE", "DEA", "FFF"])
print s.pyramidTransition("XXYX", ["XXX", "XXY", "XYX", "XYY", "YXZ"])
print s.pyramidTransition("XX", [])
print s.pyramidTransition("X", [])
print s.pyramidTransition("", [])
