'''
https://leetcode.com/problems/push-dominoes/description/

There are N dominoes in a line, and we place each domino vertically upright.

In the beginning, we simultaneously push some of the dominoes either to the left or to the right.

https://s3-lc-upload.s3.amazonaws.com/uploads/2018/05/18/domino.png

After each second, each domino that is falling to the left pushes the adjacent domino on the left.

Similarly, the dominoes falling to the right push their adjacent dominoes standing on the right.

When a vertical domino has dominoes falling on it from both sides, it stays still due to the balance of the forces.

For the purposes of this question, we will consider that a falling domino expends no additional force to a falling or already fallen domino.

Given a string "S" representing the initial state. S[i] = 'L', if the i-th domino has been pushed to the left; S[i] = 'R', if the i-th domino has been pushed to the right; S[i] = '.', if the i-th domino has not been pushed.

Return a string representing the final state. 

Example 1:

Input: ".L.R...LR..L.."
Output: "LL.RR.LLRRLL.."
Example 2:

Input: "RR.L"
Output: "RR.L"
Explanation: The first domino expends no additional force on the second domino.
Note:

0 <= N <= 10^5
String dominoes contains only 'L', 'R' and '.'
'''

class Solution(object):
    def pushDominoes(self, dominoes):
        """
        :type dominoes: str
        :rtype: str
        """
        
        # dominoes are impacted time by time, thus we need to scan several times
        # how to reduce the scan cycle?
        # maintain a list of impacting dominoes and impacting direction/area
        # impacting dominoes allow us don't need to scan full list
        # impacting direction can same checking step. e.g. R......R

        # it's much clear now, there are below scenarios:
        # ....L : keep as current
        # ....R : all are R
        # R.... : keep as current
        # L.... : all are L
        # L...R : left are L, right are R, mid is stand or empty
        # R...L : keep as current




