'''
https://leetcode.com/problems/exam-room
https://leetcode.com/articles/exam-room
In an exam room, there are N seats in a single row, numbered 0, 1, 2, ..., N-1.

When a student enters the room, they must sit in the seat that maximizes the distance to the closest person.  If there are multiple such seats, they sit in the seat with the lowest number.  (Also, if no one is in the room, then the student sits at seat number 0.)

Return a class ExamRoom(int N) that exposes two functions: ExamRoom.seat() returning an int representing what seat the student sat in, and ExamRoom.leave(int p) representing that the student in seat number p now leaves the room.  It is guaranteed that any calls to ExamRoom.leave(p) have a student sitting in seat p.

 

Example 1:


Input: ["ExamRoom","seat","seat","seat","seat","leave","seat"], [[10],[],[],[],[],[4],[]]
Output: [null,0,9,4,2,null,5]
Explanation:
ExamRoom(10) -> null
seat() -> 0, no one is in the room, then the student sits at seat number 0.
seat() -> 9, the student sits at the last seat number 9.
seat() -> 4, the student sits at the last seat number 4.
seat() -> 2, the student sits at the last seat number 2.
leave(4) -> null
seat() -> 5, the student sits at the last seat number 5.

Note:


	1 <= N <= 10^9
	ExamRoom.seat() and ExamRoom.leave() will be called at most 10^4 times across all test cases.
	Calls to ExamRoom.leave(p) are guaranteed to have a student currently sitting in seat number p.

'''
import bisect
class ExamRoom1(object):

    def __init__(self, N):
        self.N, self.L = N, []

    def seat(self):
        N, L = self.N, self.L
        if not L: res = 0
        else:
            d, res = L[0], 0
            for a, b in zip(L, L[1:]):  # get all intervals, except the last one
                if (b - a) / 2 > d:
                    d, res = (b - a) / 2, (b + a) / 2
            if N - 1 - L[-1] > d: res = N - 1   # check last interval
        bisect.insort(L, res)
        return res

    def leave(self, p):
        self.L.remove(p)

from sortedcontainers import SortedList
import collections
class ExamRoom(object):

    def __init__(self, N):
        self.region = SortedList([(N,0,N-1)])
        self.pos = {}
        self.N = N

    def seat(self):
        if not self.region: return None

        d, s, e = self.region.pop()
        s = -s

        if s == 0 or e == self.N-1:
            sitAt = 0 if s == 0 else e
        else:
            sitAt = (s + e) / 2

        self.pos[sitAt] = [None, None]
        if sitAt > s:
            left = ((sitAt+1-s)/2, -s, sitAt-1)
            self.region.add(left)
            self.pos[sitAt][0] = left
        else:
            left = None
        if s-1 in self.pos:
            self.pos[s-1][1] = left

        if e > sitAt:
            right = ((e+1-sitAt)/2, -(sitAt+1), e)
            self.region.add(right)
            self.pos[sitAt][1] = right
        else:
            right = None
        if e + 1 in self.pos:
            self.pos[e+1][0] = right
        
        return sitAt

    def leave(self, p):
        left, right = self.pos[p]
        if left and self.region:
            self.region.remove(left)
        else:
            left = (0,-p,p)

        if right and self.region:
            self.region.remove(right)
        else:
            right = (0,-p,p)

        new_region = ((left[0]+right[0]+3)/2, left[1],right[2])
        self.region.add(new_region)
        
        if -left[1]-1 in self.pos:
            self.pos[-left[1]-1][1] = new_region
        if right[2]+1 in self.pos:
            self.pos[right[2]+1][0] = new_region


# Your ExamRoom object will be instantiated and called as such:
N = 10
r1 = ExamRoom1(N)
r = ExamRoom(N)
import random
for _ in xrange(1):
    for i in xrange(10):
        assert r1.seat() == r.seat()
    arr = range(N)
    random.shuffle(arr)
    for i in arr:
        r1.leave(i)
        r.leave(i)
