# BFS/DFS and Divide-Conquer Problem
----

**\# Union Find**

    def find(seq, i):
        while seq\[i\] != i:
            seq\[i\] = seq\[seq\[i\]\]    # compression
            i = seq\[i\]
        return i

\# 递归 Recursion


1.  尾递归Tail call: 比如 n!, factorial(n) = n \* factorial (n-1)
2.  递归实现栈元素逆序
    *   递归相当于一个栈, 而实现栈颠倒至少需要2个辅助栈, 因此需要两次递归
    *   分析：乍一看到这道题目，第一反应是把栈里的所有元素逐一pop出来，放到一个数组里，然后在数组里颠倒所有元素，最后把数组中的所有元素逐一push进入栈。这时栈也就颠倒过来了。颠倒一个数组是一件很容易的事情。不过这种思路需要显示分配一个长度为O(n)的数组，而且也没有充分利用递归的特性。
    *   我们再来考虑怎么递归。我们把栈{1, 2, 3, 4, 5}看成由两部分组成：栈顶元素1和剩下的部分{2, 3, 4, 5}。如果我们能把{2, 3, 4, 5}颠倒过来，变成{5, 4, 3, 2}，然后在把原来的栈顶元素1放到底部，那么就整个栈就颠倒过来了，变成{5, 4, 3, 2, 1}。
    *   接下来我们需要考虑两件事情：一是如何把{2, 3, 4, 5}颠倒过来变成{5, 4, 3, 2}。我们只要把{2, 3, 4, 5}看成由两部分组成：栈顶元素2和剩下的部分{3, 4, 5}。我们只要把{3, 4, 5}先颠倒过来变成{5, 4, 3}，然后再把之前的栈顶元素2放到最底部，也就变成了{5, 4, 3, 2}。
    *   至于怎么把{3, 4, 5}颠倒过来……很多读者可能都想到这就是递归。也就是每一次试图颠倒一个栈的时候，现在栈顶元素pop出来，再颠倒剩下的元素组成的栈，最后把之前的栈顶元素放到剩下元素组成的栈的底部。递归结束的条件是剩下的栈已经空了。这种思路的代码如下：
    *   // Reverse a stack recursively in three steps:
    *   // 1. Pop the top element
    *   // 2. Reverse the remaining stack
    *   // 3. Add the top element to the bottom of the remaining stack
    *   template<typename T> void ReverseStack(std::stack<T>& stack)
    *   {
    *     if(!stack.empty())
    *     {
    *     T top = stack.top();
    *     stack.pop();
    *     ReverseStack(stack);
    *     AddToStackBottom(stack, top);
    *     }
    *   }
    *   我们需要考虑的另外一件事情是如何把一个元素e放到一个栈的底部，也就是如何实现AddToStackBottom。这件事情不难，只需要把栈里原有的元素逐一pop出来。当栈为空的时候，push元素e进栈，此时它就位于栈的底部了。然后再把栈里原有的元素按照pop相反的顺序逐一push进栈。
    *   注意到我们在push元素e之前，我们已经把栈里原有的所有元素都pop出来了，我们需要把它们保存起来，以便之后能把他们再push回去。我们当然可以开辟一个数组来做，但这没有必要。由于我们可以用递归来做这件事情，而递归本身就是一个栈结构。我们可以用递归的栈来保存这些元素。
    *   基于如上分析，我们可以写出AddToStackBottom的代码：
    *   // Add an element to the bottom of a stack:
    *   template<typename T> void AddToStackBottom(std::stack<T>& stack, T t)
    *   {
    *     if(stack.empty())
    *     {
    *     stack.push(t);
    *     }
    *     else
    *     {
    *     T top = stack.top();
    *     stack.pop();
    *     AddToStackBottom(stack, t);
    *     stack.push(top);
    *     }
    *   }
3.  兔子繁殖问题: 一对兔子从出生到可繁殖需两个月，然后每月都能繁殖一对兔子，问n月后共有多少兔子
    1.  终止条件: n<=2是均为1
    2.  f(n)与f(n-1)的关系: 当月兔子数 = 上个月兔子数 + 上个月可以繁殖的兔子数 (即上上月的兔子总数)





\# 分治


1.  二分搜索
2.  合并排序
3.  快速排序
4.  
5.  大整数乘法: 两个大整数相乘
    1.  将大整数分解成多块, 比如X = A|B|C, Y=D|E|F, ‘|'表示字符相连, X\*Y的问题就是(A|B|C) \* (D|E|F)相对小整数相乘
6.  Strassen矩阵乘法 <算法导论 chapter 28>
    1.  https://www.jianshu.com/p/6e21f8e872fd
7.  棋盘覆盖
    1.  在一个2k×2k个方格组成的棋盘中,若有一个方格与其他方格不同,则称该方格为一特殊方格,且称该棋盘为一个特殊棋盘. 在棋盘覆盖问题中，要用下图中 4 中不同形态的L 型骨牌覆盖一个给定的特殊棋牌上除特殊方格以外的所有方格，且任何 2 个 L 型骨牌不得重叠覆盖. https://www.jianshu.com/p/97b09ef06735
8.  线性时间选择
    1.  线性时间选择第i大的元素: 将数组分成5个元素一组, 插入排序, 选取所有组的中位数的中位数x, 有一部分区域肯定比x大/小, 假设x排序位置为k, 比较i与k大小决定下一步递归. <算法导论p112>
9.  最接近点对问题
    1.  [https://blog.csdn.net/liufeng\_king/article/details/8484284](https://blog.csdn.net/liufeng_king/article/details/8484284)
10.  循环赛日程表
    1.  https://blog.csdn.net/u014755255/article/details/50570563
11.  汉诺塔



----

- Date: 2018-10-03
- Tags: #note #Interview/Programing 



