'''
https://leetcode.com/problems/minimum-window-substring/description/

Given a string S and a string T, find the minimum window in S which will contain all the characters in T in complexity O(n).

Example:

Input: S = "ADOBECODEBANC", T = "ABC"
Output: "BANC"
Note:

If there is no such window in S that covers all characters in T, return the empty string "".
If there is such window, you are guaranteed that there will always be only one unique minimum window in S.
'''

from collections import Counter
import sys
class Solution:
    def minWindow(self, S, T):
        counter = Counter(T)

        remain_size, begin, end, l, head = len(T), 0, 0, sys.maxint, 0

        
        while end < len(S):
            if counter[S[end]] > 0:
                remain_size -= 1
            counter[S[end]] -= 1
            
            while remain_size == 0:
                if end - begin < l:
                    l = end - begin
                    head = begin
                if counter[S[begin]] == 0:
                    remain_size += 1
                counter[S[begin]] += 1
                begin += 1

            end += 1
        return S[head:head+l+1] if l < sys.maxint else ""


from collections import deque
class Solution3:
	def minWindow(self, S, T):
		letterC = {}
		for c in T:
			if c not in letterC: letterC[c] = 0
			letterC[c] += 1

		l = r = 0
		ans, cache = None, {}
		minLen = len(letterC.keys())
		while l <= len(S) - minLen and r < len(S):
			c = S[r]
			if c not in letterC:
				if l == r: l += 1
				r += 1
				continue

			# cache directory keep the letter and its corresponding positions
            # use deque for efficient append and popleft
			if c not in cache: cache[c] = deque()
			cache[c].append(r)
			
			if len(cache[c]) > letterC[c]:
				# when substring contain more this letter, we can consider
                # to popleft some letter previous, while only when the first
                # letter is the same one, otherwise we might strip other letters
				if l == cache[c][0]:
					candidate_l = cache[c][1]
					cache[c].popleft()
					for i in range(l+1, candidate_l):
						x = S[i]
						if x not in letterC: continue
						if len(cache[x]) > letterC[x]:
							cache[x].popleft()
						else:
							l = i
							break
					else:
						l = candidate_l
			
			if len(cache[c]) >= letterC[c]:
				for letter,count in letterC.iteritems():
					if letter not in cache or len(cache[letter]) < letterC[letter]:
						break
				else:
					if not ans or r + 1 - l < len(ans):
						ans = S[l:r+1]

			r += 1

		return ans if ans else ""

# 48ms soluton, mine is 536ms
class Solution2(object):
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        # Defaultdict is very useful in this problem, though i don't like to import modules
        target_count_dict = collections.defaultdict(int)
        for ch in t:
            target_count_dict[ch] += 1
        remain_missing = len(t)
        start_pos, end_pos = 0, float('inf')
        current_start = 0
        
        # Enumerate function makes current_end indexes from 1
        for current_end, ch in enumerate(s, 1):
            # Whenever we encounter a character, no matter ch in target or not, we minus 1 in count dictionary
            # But, only when ch is in target, we minus the length of remain_missing
            # When the remain_missing is 0, we find a potential solution.
            if target_count_dict[ch] > 0:
                remain_missing -= 1
            target_count_dict[ch] -= 1
            
            if remain_missing == 0:
                # Remove redundant character
                # Try to find the fist position in s that makes target_count_dict value equals 0
                # Which means we can't skip this character in s when returning answer
                while target_count_dict[s[current_start]] < 0:
                    target_count_dict[s[current_start]] += 1
                    current_start += 1
                if current_end - current_start < end_pos - start_pos:
                    start_pos, end_pos = current_start, current_end
                
                # We need to add 1 to current_start, and the correspondence value in dictionary, is because
                # this is the first character of the potential answer. So, in future iteration, when we encounter this character,
                # We can remove this currently first character to try to find a shorter answer.
                target_count_dict[s[current_start]] += 1
                remain_missing += 1
                current_start += 1
        
        return s[start_pos:end_pos] if end_pos != float('inf') else ""


import random
s = Solution()
S = "".join(map(lambda i: chr(ord('A') +i), [random.randint(0, 10) for _ in range(10000)]))
T = "".join(map(lambda i: chr(ord('A') +i), [random.randint(0, 10) for _ in range(30)]))

print S
print T
print s.minWindow(S, T)
