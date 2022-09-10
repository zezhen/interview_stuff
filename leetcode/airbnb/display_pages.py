
'''
This    is  well    known   as  OA2.
http://www.1point3acres.com/bbs/forum.php?mod=viewthread&tid=278720
You’re  given   an  array   of  CSV strings representing    search  results.    Results are sorted  by  a   score   initially.  A   
given   host    may have    several listings    that    show    up  in  these   results.    Suppose we  want    to  show    12  results 
per page,   but we  don’t   want    the same    host    to  dominate    the results.    Write   a   function    that    will    reorder 
the list    so  that    a   host    shows   up  at  most    once    on  a   page    if  possible,   but otherwise   preserves   the ordering.   
Your    program should  return  the new array   and print   out the results in  blocks  representing    the pages.  
Input: An   array   of  csv strings,    with    sort    score   number  of  results per page.   example:    
"host_id,listing_id,score,city" 
"1,28,300.1,San Francisco"


5
13
1,28,310.6,SF   
4,5,204.1,SF    
20,7,203.2,Oakland  
6,8,202.2,SF
6,10,199.1,SF   
1,16,190.4,SF   
6,29,185.2,SF   
7,20,180.1,SF   
6,21,162.1,SF
2,18,161.2,SF   
2,30,149.1,SF
3,76,146.2,SF   
2,14,141.1,San  Jose
以上是一个 Sample    输入，和希望的输出，1,28,100.3,Paris  代表 Host ID, List    ID, Points, City.   这是
Airbnb 根据用户搜索条件得出的一些 list，然后我们要分页，第一行的 5 代表每一页最多展示 5 个
list，13 应该是代表有 13 个 List.所以我们是要分成 3 页。规则是：每一页最多展示一个 host 的
list，但是如果再没有其他 host 的 list 可以展示了，就按照原有的顺序填补就可（根据 Points，也
就是排名）。应得到的输出：
希望输出：
1,28,310.6,SF
4,5,204.1,SF
20,7,203.2,Oakland
6,8,202.2,SF    
7,20,180.1,SF   
6,10,199.1,SF   
1,16,190.4,SF   
2,18,161.2,SF
3,76,146.2,SF   
6,29,185.2,SF -- 这时不得不重复了，从原有队列拉出第一个
6,21,162.1,SF
2,30,149.1,SF
2,14,141.1,San  Jose
'''


import collections
def arrage(n, array):
    p = len(array) / n + 0
    if len(array) % n != 0:
        p += 1

    pages = []
    for i in xrange(p):
        pages.append(collections.deque())

    id_placer = {}
    start = 0

    for item in array:
        _id = item.split(',')[0]

        index = id_placer[_id] if _id in id_placer else start
        
        pages[index].append(item)
        id_placer[_id] = min(index + 1, p-1)
        if index == start and len(pages[index]) == n:
            start += 1

    for i in xrange(p-1):
        j = i + 1
        while len(pages[i]) < n:
            while len(pages[j]) <= 0:
                j += 1
            pages[i].append(pages[j].popleft())

    return map(list, pages)

res = arrage(5, ['1,28,310.6,SF', '4,5,204.1,SF', '20,7,203.2,Oakland', '6,8,202.2,SF', '6,10,199.1,SF', '1,16,190.4,SF', '6,29,185.2,SF', '7,20,180.1,SF', '6,21,162.1,SF', '2,18,161.2,SF', '2,30,149.1,SF', '3,76,146.2,SF', '2,14,141.1,SanJose'])
for l in res:
    print l