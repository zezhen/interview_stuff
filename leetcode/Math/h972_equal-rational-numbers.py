'''
https://leetcode.com/problems/equal-rational-numbers/description/

Given two strings S and T, each of which represents a non-negative rational number, return True if and only if they represent the same number. The strings may use parentheses to denote the repeating part of the rational number.

In general a rational number can be represented using up to three parts: an integer part, a non-repeating part, and a repeating part. The number will be represented in one of the following three ways:

<IntegerPart> (e.g. 0, 12, 123)
<IntegerPart><.><NonRepeatingPart>  (e.g. 0.5, 1., 2.12, 2.0001)
<IntegerPart><.><NonRepeatingPart><(><RepeatingPart><)> (e.g. 0.1(6), 0.9(9), 0.00(1212))
The repeating portion of a decimal expansion is conventionally denoted within a pair of round brackets.  For example:

1 / 6 = 0.16666666... = 0.1(6) = 0.1666(6) = 0.166(66)

Both 0.1(6) or 0.1666(6) or 0.166(66) are correct representations of 1 / 6.

 

Example 1:

Input: S = "0.(52)", T = "0.5(25)"
Output: true
Explanation:
Because "0.(52)" represents 0.52525252..., and "0.5(25)" represents 0.52525252525..... , the strings represent the same number.
Example 2:

Input: S = "0.1666(6)", T = "0.166(66)"
Output: true
Example 3:

Input: S = "0.9(9)", T = "1."
Output: true
Explanation: 
"0.9(9)" represents 0.999999999... repeated forever, which equals 1.  [See this link for an explanation.]
"1." represents the number 1, which is formed correctly: (IntegerPart) = "1" and (NonRepeatingPart) = "".
 

Note:

Each part consists only of digits.
The <IntegerPart> will not begin with 2 or more zeros.  (There is no other restriction on the digits of each part.)
1 <= <IntegerPart>.length <= 4
0 <= <NonRepeatingPart>.length <= 4
1 <= <RepeatingPart>.length <= 4
'''

class Solution(object):
    def isRationalEqual(self, S, T):
        """
        :type S: str
        :type T: str
        :rtype: bool
        """
        def removeZero(N, fromHead=True):
            if not N: return N
            i,d = (0, 1) if fromHead else (len(N)-1, -1)
            while 0 <= i < len(N) and N[i] == '0':
                i += d
            return N[i:] if fromHead else N[:i+1]

        def inc(N):
            _len = len(N)
            res = str(int(N) + 1)
            return '0' * (_len - len(res)) + res

        def cmp_rep(rep1, rep2):
            if len(rep1) > len(rep2):
                rep1, rep2 = rep2, rep1
            if len(rep2) % len(rep1) != 0: return False

            return rep1 * (len(rep2) / len(rep1)) == rep2
        
        def parse(N):
            integer,nonRep, rep = N, '0', '0'
            if '.' in N:
                integer, nonRep = N.split('.')
                if not integer: integer = '0'
                if not nonRep: nonRep = '0'
            
            if '(' in nonRep:
                i = nonRep.index('(')
                nonRep, rep = nonRep[:i], nonRep[i+1:-1]
                
                # processing (666) (999) case, (696969)
                if len(set(rep)) == 1:
                        rep = rep[0]

                
                if rep == '9':   # carry over to nonRep
                    if not nonRep or set(nonRep) == set('9'): # carry over to integer part
                        integer = str(int(integer) + 1)
                        nonRep = '0'
                    else:
                        nonRep = inc(nonRep)
                    rep = '0'
                else:
                    shrink = 0
                    for d in nonRep[::-1]:
                        if rep.endswith(d):
                            rep = d + rep[:-1]
                            shrink += 1
                    if shrink > 0:
                        nonRep = nonRep[:-shrink] if shrink < len(nonRep) else '0'

            return (removeZero(integer), removeZero(nonRep, False), rep)
        
        int1, nonrep1, rep1 = parse(S)
        int2, nonrep2, rep2 = parse(T)
        print (int1, nonrep1, rep1)
        print (int2, nonrep2, rep2)
        return (int1, nonrep1) == (int2, nonrep2) and cmp_rep(rep1, rep2)
                        
s = Solution()
# print s.isRationalEqual("13","13") == True
# print s.isRationalEqual("1.0","1") == True
# print s.isRationalEqual("1.0(1)","1.0(1)") == True
# print s.isRationalEqual("1.01(1)","1.0(1)") == True
# print s.isRationalEqual("1.012(12)","1.0(12)") == True
# print s.isRationalEqual("1.01(21)","1.0(12)") == True
# print s.isRationalEqual("01.01(9)","1.02") == True
# print s.isRationalEqual(".01(9)","0.02") == True
# print s.isRationalEqual(".(9)","1.0") == True
# print s.isRationalEqual("0.1666(6)", "0.166(66)") == True
# print s.isRationalEqual("0.(0)", "0") == True
# print s.isRationalEqual("250.(36)", "250.(3636)") == True
# print s.isRationalEqual("8.123(4567)", "8.123(4566)") == False

print s.isRationalEqual("550.(1515)", "550.(15)")
