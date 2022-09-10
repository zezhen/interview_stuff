# -*- coding: utf-8 -*-
'''

猜一个4位的数字，每位上数字从1到9.
提供一个API，输入一个你猜的数字，返回有几位是猜对的。
比如要猜的数字是1234，猜的数字是1111，则返回1
猜的数字是1212，则返回2
要求写个程序多次调用这个API以后，返回猜的数字结果是什么.

'''
target = '1454'
from collections import Counter

def api1(number):
    counter = Counter(target) & Counter(number)
    return len(list(counter.elements()))

print api1('4444')

def guess1():
    candidate = []
    for i in xrange(10):
        c = api1(str(i)*4)
        while c > 0:
            candidate.append(i)
            c -= 1
    return candidate


def api2(number):
    match = contain = 0
    for i,e in enumerate(number):
        if e == target[i]:
            match += 1
        elif e in target:
            contain += 1
    return match, contain

def guess2():
    candidate = []
    for i in xrange(10):
        m, c = api2(str(i)*4)
        while m > 0:
            candidate.append(i)
            m -= 1

    def dfs(nums,path):
        if len(nums) == 0:
            return path if api2(''.join(map(str,path))) == (4, 0) else None

        for i in range(len(nums)):
            res = dfs(nums[:i]+nums[i+1:],path + [nums[i]])
            if res: return res

    return ''.join(map(str, dfs(candidate,[])))

print guess1()
print guess2()