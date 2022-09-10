'''
https://leetcode.com/problems/remove-invalid-parentheses
https://leetcode.com/articles/remove-invalid-parentheses
Remove the minimum number of invalid parentheses in order to make the input string valid. Return all possible results.

Note: The input string may contain letters other than the parentheses ( and ).

Example 1:


Input: "()())()"
Output: ["()()()", "(())()"]


Example 2:


Input: "(a)())()"
Output: ["(a)()()", "(a())()"]


Example 3:


Input: ")("
Output: [""]
'''

class Solution(object):
    def removeInvalidParentheses(self, s, pars=['(', ')']):
        """
        :type s: str
        :rtype: List[str]
        """

        # scan s from left to right, count number of ( and )
        # if there is extra ')' at position i, we will know immediately
        #     we have multiple choice to remove either one ), after remove we can recursively call next
        #     one thing important is that we need to record the scan position and remove position for next recursion
        #     scan position guarantees we don't need to scan the position we already checked
        #     remove position states the next possible remove position in next recursion to avoid duplicated check.
        # if there is extra '(' error, we can know until reach end
        #     then look back, similar like process ')' issue
        # how about characters?  no impact on the parentheses valid

        ans = []
        def remove(s, remove_i, scan_i, pars):
            count = 0
            for i in xrange(scan_i, len(s)):
                if s[i] == pars[0]:
                    count += 1
                elif s[i] == pars[1]:
                    count -= 1

                if count < 0:
                    for j in xrange(remove_i, i+1):
                        if s[j] == pars[1] and (j == remove_i or s[j-1] != pars[1]):
                            remove(s[:j]+s[j+1:], j, i, pars)
                    return

            if count == 0:
                ans.append(s if pars[0] == '(' else s[::-1])

            if count > 0 and pars[0] == '(':
                remove(s[::-1], 0, 0, [')', '('])

        remove(s, 0, 0, ['(', ')'])
        return ans

s = Solution()
print s.removeInvalidParentheses('()())()') == ['(())()', '()()()']
print s.removeInvalidParentheses('x(')  == ['x']
print s.removeInvalidParentheses('(r(()()(') ==  ['(r())', 'r(())', '(r)()', 'r()()']
print s.removeInvalidParentheses('()()()') == ['()()()']
print s.removeInvalidParentheses('(a)())()')
print s.removeInvalidParentheses('((()()()')

# public List<String> removeInvalidParentheses(String s) {
#     List<String> ans = new ArrayList<>();
#     remove(s, ans, 0, 0, new char[]{'(', ')'});
#     return ans;
# }

# public void remove(String s, List<String> ans, int last_i, int last_j,  char[] par) {
#     for (int stack = 0, i = last_i; i < s.length(); ++i) {
#         if (s.charAt(i) == par[0]) stack++;
#         if (s.charAt(i) == par[1]) stack--;
#         if (stack >= 0) continue;
#         for (int j = last_j; j <= i; ++j)
#             if (s.charAt(j) == par[1] && (j == last_j || s.charAt(j - 1) != par[1]))
#                 remove(s.substring(0, j) + s.substring(j + 1, s.length()), ans, i, j, par);
#         return;
#     }
#     String reversed = new StringBuilder(s).reverse().toString();
#     if (par[0] == '(') // finished left to right
#         remove(reversed, ans, 0, 0, new char[]{')', '('});
#     else // finished right to left
#         ans.add(reversed);
# }