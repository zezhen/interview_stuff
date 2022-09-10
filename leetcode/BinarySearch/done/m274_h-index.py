'''
https://leetcode.com/problems/h-index/description/

Given an array of citations (each citation is a non-negative integer) of a researcher, write a function to compute the researcher's h-index.

According to the definition of h-index on Wikipedia: "A scientist has index h if h of his/her N papers have at least h citations each, and the other N − h papers have no more than h citations each."

Example:

Input: citations = [3,0,6,1,5]
Output: 3 
Explanation: [3,0,6,1,5] means the researcher has 5 papers in total and each of them had 
             received 3, 0, 6, 1, 5 citations respectively. 
             Since the researcher has 3 papers with at least 3 citations each and the remaining 
             two with no more than 3 citations each, her h-index is 3.
Note: If there are several possible values for h, the maximum one is taken as the h-index.
'''

class Solution(object):
    def hIndex(self, citations):
        """
        :type citations: List[int]
        :rtype: int
        """

'''
sorting need at least O(nlogn) time

apply n+1 length array count, count[i] means the count of paper has i cictations
if the citation of one paper is greater than n, add 1 to count[n]

scan from tail, use a number acc to accumulate the paper count, find the first i that acc >= i

'''        


        citations.sort(reverse=True)
        i = len(citations) - 1
        hindex = 0
        while i >= 0 and i + 1 > hindex:
            hindex = max(hindex, min(citations[i], i+1))
            i -= 1
        return hindex