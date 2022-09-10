# Sorting Problem
----

*   堆排序 O(nlgn)
    *   图1为最大堆(最小堆一般用于优先级队列), 树形或数组, 从1开始记位, 结点i, 其父节点为i/2, 左子结点为2i, 右子结点为2i+1
    *   保持堆性质: 对结点i, 比较本身和左右子结点, 选取最大的替换i, 递归向下替换
    *   建堆: 从n/2->1, 相当于从叶节点的父节点开始, 依次处理使其保持堆性质, 直到根结点
    *   堆排序: 交换堆顶元素和最小值, 并保持堆性质, 树/数组大小减1
    *   ![[Archive/面试资料/Programming/_resources/Sorting_Problem.resources/unknown_filename.6.png]]![[Archive/面试资料/Programming/_resources/Sorting_Problem.resources/unknown_filename.png]]![[Archive/面试资料/Programming/_resources/Sorting_Problem.resources/unknown_filename.3.png]]
*   快速排序 O(nlgn)
    *   PARTITION中A\[p\]~A\[i\]均小于A\[r\], HOARE是最早学的那种, 两端扫描交换, STOOGE则分别排序前2/3, 后2/3, 前2/3
    *   ![[Archive/面试资料/Programming/_resources/Sorting_Problem.resources/unknown_filename.7.png]]![[Archive/面试资料/Programming/_resources/Sorting_Problem.resources/unknown_filename.5.png]]![[Archive/面试资料/Programming/_resources/Sorting_Problem.resources/unknown_filename.9.png]]![[Archive/面试资料/Programming/_resources/Sorting_Problem.resources/unknown_filename.2.png]]



*   线性时间排序: 计数,基数, 桶排序
    *   比较排序可抽象为一个决策树, 其下界是O(nlgn)
    *   计数排序: 假设元素介于0~k的整数, 对每个元素x, 确定小于x的元素个数, 把x直接放到最终输出数组的位置上即可
    *   基数排序
        *   按位排序, 从最低位开始排序, 如图2, 需要稳定排序. 如果每一个位数可以取k种可能, 可采用计数排序, 其复杂度为O(n+k), 总复杂度为O(d(n+k)). 
        *   给定n个b位数和任何正整数r<=b, 采用线性稳定排序, 基数排序的复杂度为O((b/r)(n+2^r)), 取b=O(lgn), r约为lgn, 基数排序时间线性! 
        *   基数排序执行遍数可能比快排少, 但每一遍所化时间都要长得多, 要看底层机器实现特性, 如快排可以有效利用硬件缓存; 计数排序不是就地排序, 若内存吃紧, 快排相对更好
    *   桶排序: 将区间\[0, 1)换分成n个大小相同的子区间(桶), 将n个输入数据分布到桶中. 需要O(n)的空间, 如果各个桶的尺寸的平方和与n线性相关, 则桶排序复杂度为O(n)
    *   ![[Archive/面试资料/Programming/_resources/Sorting_Problem.resources/unknown_filename.1.png]]![[Archive/面试资料/Programming/_resources/Sorting_Problem.resources/unknown_filename.8.png]]![[Archive/面试资料/Programming/_resources/Sorting_Problem.resources/unknown_filename.4.png]]
*   中位数和顺序统计学

1.  最小值和最大值
    1.  求n个元素的最值需要n-1次比较(这个是必须的),  无论是线性扫描还是两两比较(n/2+n/4+...+1)
    2.  同时求最大值和最小值则可以有所优化, 即两两比较后即可得到n/2的大值和n/2的小值, 再分别线性比较(没有必要继续两两, 代价是一样的), 需要\[3n/2\]-2(向上取整)次比较
2.  以期望线性时间做选择
    1.  以快排算法为模型, 选择第k大的元素. 快排采用随机划分的方式, 最坏情况复杂度为O(n^2), 但平均情况下, 对任何顺序统计量(特别是中位数)是线性的
3.  最坏线性时间的选择
    1.  将n个元素按每组5个元素划分, 剩余的元素自成一组; 对每组插入排序找出中位数; 再递归调用SELECT算法找出中位数的中位数x\[偶数则为下中位数\]; 利用PARTITION算法, x为povit进行划分, 在利用SELECT算法找到第i个元素
    2.  如图阴影所示, x右侧5元素的数组至少有3个数大于x, 大于x的树至少为3n/10-6, 同理至少有3n/10-6个数小于x. 该算法最坏是线性的(证明略)
4.  寻找n个元素的top k个大值
    1.  先排序+列出k个最大值 O(nlgn)
    2.  建立优先级队列, 从堆顶取k次 O(klgn)
    3.  利用顺序统计量算法找到第k个最大元素, 然后划分输入数组, 对k个最大值排序 O(n)
5.  ![[Archive/面试资料/Programming/_resources/Sorting_Problem.resources/unknown_filename.12.png]]![[Archive/面试资料/Programming/_resources/Sorting_Problem.resources/unknown_filename.11.png]]![[Archive/面试资料/Programming/_resources/Sorting_Problem.resources/unknown_filename.10.png]]

*   多路归并+败者树
    *   多路归并和普通的合并算法相似, 只是k路而不是两路, 其中k路中最小值的选择可以用线性, 用最大堆, 或败者树. 线性比较需要k-1次, 最大堆从上往下更新, 在每个节点处均要和左右子节点比较, 而败者树则是从下往上更新, 比较相对较少, 改动的结点少, 如上图所示.两结点比较, 败者作为父节点, 胜者继续往上比较
    *   多路归并败者树 (python)
        1.  def mergeKLists(K):
        2.      MIN, MAX = - sys.maxint, sys.maxint
        3.  
        4.      def adjust\_tree(base, tree, s):
        5.   t = (s + K) / 2
        6.          while t > 0:
        7.              if base\[s\] > base\[tree\[t\]\]:
        8.                  tree\[t\], s = s, tree\[t\]
        9.              t /= 2
        10.          tree\[0\] = s
        
        12.      base = \[\]
        13.      for i in xrange(K):
        14.          base.append(get\_next(i))
        15.      base.append(MIN) # placeholder
        16.  
        17.      tree = \[K\] \* K  # point to minimum value
        18.      for i in range(K)\[::-1\]:
        19.          adjust\_tree(base, tree, i)
        20.  
        21.      ans = \[\]
        22.      while base\[tree\[0\]\] != MAX:
        23.          ans.append(base\[tree\[0\]\])
        24.          base\[tree\[0\]\] = get\_next(tree\[0\])    # get\_next return MAX if list become empty
        25.          adjust\_tree(base, tree, tree\[0\])
        26.      return ans
    *   败者树的重点在于adjust\_tree这个函数, 首先需要明白的是, 树的结构跟K的奇偶性有关系, 关键是t = (s+K)/2, 如下图所示, 当K=3时, index=1和2共享一个父节点, 当K=4时, 0/1和2/3各自共享父节点;
    *   当base\[s\] > base\[tree\[t\]\], 即子节点败给父节点, 则将tree\[t\]替换为s, 将原来的tree\[t\]上浮, 继续比较知道0
    *   初始化base中添加一个MIN作为placeholder, tree所有节点指向该MIN, 然后挨个adjust, 即可上浮
        *   ![[Archive/面试资料/Programming/_resources/Sorting_Problem.resources/unknown_filename.13.png]]
*   [[O(1)空间复杂度的归并排序.md|O(1)空间复杂度的归并排序]]
    1.  循环换位合并法: 可以实现
    2.  内部缓存法: 太复杂, 理解就行
*   搜索
    *   数组二分搜索, 树的二叉搜索, 图的广度/深度优先以及A\*算法, 回溯剪枝算法
*   变形

1.  合并排序变形: 数组n前后两部分已排好序, 要求O(1)空间, O(n)时间合并
    *   内部缓存法, 见网摘
2.  二分查找: 如789123456 \[ http://www.cnblogs.com/rocketfan/archive/2009/09/19/1570149.html\]
    *   l=3, r=2, m=(l+r+n)/2%n
3.  2个有序数组, 求合并后的第k大



----

- Date: 2012-09-09
- Tags: #note #Interview/Programing 
- Source URL: [](http://chenkegarfield.blog.163.com/blog/static/62330008200910249526638/)



