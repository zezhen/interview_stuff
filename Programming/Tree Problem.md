# Tree Problem
----

*   平衡二叉树
    *   [Design HashSet](https://leetcode.com/problems/design-hashset)
    *   [Design HashMap](https://leetcode.com/problems/design-hashmap)
*   [Verify Preorder in bst](https://leetcode.com/problems/verify-preorder-sequence-in-binary-search-tree)
    *   inorder? postorder?



1.  遍历和查找
    1.  二叉树两节点的公共祖先LCA
        1.  自顶向下: 从根节点出发, 依次查看左右两树是否包含节点p和q, 如果左右各包含一个, 则LCA为根节点, 否则进入左或右树查看 O(N^2)
        2.  自底向上: 递归搜索p和q, 找到p/q则向上传递, 父节点根据左右两侧传递的节点来决定上传自己作为LCA, 或者左右两边的非null部分
        3.  公共路径: 搜索从根节点到p和q的路径, 然后计算公共路径
    2.  二叉树最深/浅的路劲长
        1.  递归计算左右两树的最深/浅路径长度, 然后各+1返回, 合并左右子树时取最大的大数, 最小的小数
        2.  迭代: 层次遍历, 记录一个level值, 如果某个节点为叶子节点, 记录level大小以及和max/min比较
    3.  前/中/后序遍历
        1.  递归方式比较简单
        2.  迭代方式
            1.  前序: 需要辅助栈, 从根节点开始, 不断插入左节点直到结束, 在插入栈的时候即可访问, 然后从栈顶取出元素, 检查其右节点, 重复插入其左节点, 直到栈为空
            2.  中序: 类似前序, 只不过访问节点在从栈顶取元素的时候发生
            3.  后序: 类似中序, 需要维持一个上一次访问节点的指针, 然后在从栈顶取元素前, 检查改元素的右节点是否为空或者为上一个访问节点, 如果是则进行访问并弹出, 否则将这个右节点加入栈中, 继续加入其左节点.
    4.  前/中/后序列间的变换
        1.  先序+中序->后序: 由先序第一个元素为根结点, 对应中序根结点在第k个位置, 则0-k-1为左子树, k+1-n-1为右子树
        2.  后序+中序->先序: 由后序最后一个元素为根结点, 对应中序根结点在第k个位置, 则0-k-1为左子树, k+1-n-1为右子树
        3.  先序+后续->中序: 多个 参考[construct-binary-tree-from-preorder-and-postorder-traversal](https://leetcode.com/problems/construct-binary-tree-from-preorder-and-postorder-traversal/description/)
    5.  层次遍历
        
        *   需要队列辅助, 需要marker来表示该层已经结束, 然后重新加入队列中 (出队入队比较耗时, 用head/tail指针标识对头对尾即可)
        
        1.  def levelOrder(self, root):
        2.      if root == None: return \[\]
        3.  
        4.      ans, queue = \[\[root.val\]\], \[root\]
        5.      head, tail = 0, len(queue)
        6.      while head < len(queue):
        7.          node = queue\[head\]
        8.          head += 1
        9.  
        10.          if node.left:
        11.              queue.append(node.left)
        12.          if node.right:
        13.              queue.append(node.right)
        14.  
        15.          if head == tail:
        16.              tail = len(queue)
        17.              if tail > head:
        18.                  ans.append(map(lambda n:n.val, queue\[head:tail\]))
        19.      return ans
    
    *   当给节点加一个next指针指向右侧同层节点时, 如何设置next?
    
    1.  def connect(self, root):
    2.      start, node = TreeLinkNode(0), root
    3.      while node:
    4.          start.next = None  #reset
    5.          current = start
    6.          while node:
    7.              if node.left:
    8.                  current.next = node.left
    9.                  current = current.next
    10.              if node.right:
    11.                  current.next = node.right
    12.                  current = current.next
    13.              node = node.next
    14.          node = start.next  # start points to the first node in each level
    15.      return root
    
    8.  将查找二叉树变成有序的双向链表
        1.  查找二叉树的先序遍历即为有序
    9.  二叉树第K层的节点个数
        1.  层次遍历到第K层
    10.  二叉树中叶子节点的个数
        1.  任意一种遍历, 叶子节点判断条件是左右子节点均为空
    11.  路劲查找: 路径节点值的和为T
        1.  backtracking, 如果均为正整数, 若大于T则结束, 否则需要访问整棵树
    12.  给定x,y, 在二叉搜索树中找出区间的所有节点
        1.  递归搜索, 如果根节点大小在区间内, 则两边搜索, 否则只搜一遍
    13.  string和tree转换
        1.  [construct-binary-tree-from-string](https://leetcode.com/problems/construct-binary-tree-from-string/description/): 4(2(3)(1))(6(5)) to tree
        2.  
    14.  ==打印二叉树==
        1.  
2.  比较/判断
    1.  二叉树是否为平衡二叉树: 左右两子树深度差不超过1
        1.  递归计算左右两子树深度差, 如果大于1则不是平衡树
    2.  二叉树是否为完全二叉树
        *   完全二叉树只允许最后一层的最右侧有空位, 所以1) 右子树存在左子树为空, 则一定非,  2) 层次遍历, 遇到第一个右子树为空的节点, 那之后所有节点均为叶子节点, 否则一定非
    3.  ==拓扑结构(什么是拓扑结构?==)相同子树: 判断t1树中是否有与t2树拓扑结构完全相同的子树
        1.  将t1和t2序列化成字符串, 比如先序遍历, 把问题变成字符串匹配问题, 注意重复字符串内容的情况
3.  特殊结构
    1.  二叉查找树 : 对任意结点x, 其左子树中关键字不超过key\[x\], 其右子树中的关键字最小不小于key\[x\], 采用中序遍历将得到一个有序序列.
        *   查找: 类似二分查找, 查找x与key\[x\]比较, 大则查找右子树, 小则查找左子树, O(lgn)
        *   树最值: 最小值是最左侧结点, 最大值为最右侧结点
        *   前驱和后继: 为中序遍历的前驱和后继结点. 后继: 如果存在右子树, 其后继为右子树最小值; 否则后继y将是x的最低祖先结点, 并且y的左儿子也是x的祖先. (对y来说, x是其左子树的最大值, 即其前驱). 后继结点正好相反.
        *   插入结点z: 沿根下降直到某个叶结点x, 然后将z设为x的左/右结点, 更新z的父节点指向x
        *   删除结点z: 若z无子女, 则直接删除, 更新其父节点的子节点为NULL; 若z只有一个子女, 链接其父节点和子节点即可; 若有两个子女, 删除z的后继y, 并用y的内容替换z的内容. (TREE-DELETE: 1~3确定要删除的结点, z本身or其后继, 4~6中x被设置为y的非NULL子女或NULL, 7~13通过p\[y\]和x删除y, 最后复制y的内容)
    2.  堆
        1.  最大堆: (二叉树形式) 所有父节点都比两个子节点大.
    3.  红黑树  https://www.cnblogs.com/wuchanming/p/4444961.html
        1.  红黑树性质: 结点为红色或黑色; 根节点和叶结点为黑色; 若红结点的两个子结点均为黑色; 对每个结点, 从该结点到子孙结点的所有路径上包含相同数目的黑结点. 
        2.  高度: 一颗有n个内结点的RB-tree高度至多为2lg(n+1)
        3.  左右旋转: 在插入和删除之后, 可能无法保证红黑树性质,需要通过旋转来修改指针结构
        4.  插入: 插入z后需要保证红黑树性质, 故增加了RB-INSERT-FIXUP过程,  插入的z为红, 若其父节点也为红(行1), 则破坏性质3, 先处理z的父节点是其爷结点的左结点(行2), y指向z的叔结点, 如果y为红色(case 1, 如图4), 将y以及z的父节点改为黑, 爷结点为红, 用z指向爷结点, 继续执行; 若y为黑, 若z是父节点的右孩子(case 2, 如图5), 通过左旋将其转为左孩子(case 3), 最后再改颜色+右旋完成操作, 能保证性质.
        5.  删除: RB-DELETE(T,z)真正删除的y(z本身或其后继), 如果y为黑色, 则需要调用RB-DELETE-FIXUP(T, x), 其中x是y的非空子树. y删除后可能破坏性质4, 故而假设x指向的结点有额外的黑色. 
    
    *   如何保证相同数目的黑色, 可以在x前插入黑色, 这个需要左旋, 如图2, x指针指向alpha(不是图中的x), 需要多一个黑色, 左旋之后, color\[y\]<-color\[x\], 将x设为黑, alpha多出一个黑色, 此时需要保证y是黑色, 不然beta将多一个黑色(需要case 1保证), 而此时gama少了一个黑色, 需要保证其根结点为红色, 然后更新为黑色, 就可以保证性质4了(如case 4), 但若gama的根结点为黑色, 我们看看其左子树是否为红色, 若是则可以通过右旋使其左子树的红根为根(case 3), 否则我们讲额外的黑色上移, 交给父节点处理, 此时图2中x结点多了一个黑色, 需要保证y也是黑色, 将其设为红即可(case 2), 所以case1是所有操作的前提.
    *   具体操作如下: case 1保证x的兄弟y为黑色; case 2不能内部搞定, 将额外黑色上移; case 3保证case 4能够为x前添加一个黑色结点.
    *   ![[Archive/面试资料/Programming/_resources/Tree_Problem.resources/unknown_filename.png]]![[Archive/面试资料/Programming/_resources/Tree_Problem.resources/unknown_filename.3.png]]![[Archive/面试资料/Programming/_resources/Tree_Problem.resources/unknown_filename.2.png]]
    *   ![[Archive/面试资料/Programming/_resources/Tree_Problem.resources/unknown_filename.1.png]]
    *   ![[Archive/面试资料/Programming/_resources/Tree_Problem.resources/unknown_filename.5.png]]![[Archive/面试资料/Programming/_resources/Tree_Problem.resources/unknown_filename.4.png]]
    
    5.  B族树: B树, B+树, B\*树, R树
        1.  B树: 为磁盘等设计的一种查找平衡树, 其结点通常相当于一个完整的磁盘页
            *   每个结点x包含n\[x\]个关键字和n\[x\]+1个子女, 关键字按非降序存放; 每个叶结点有相同的深度(平衡树); 结点关键字个数在区间\[t-1, 2t-1\], t为B树的最小读数, 2t-1认为是B树的阶(奇数, 如此在分裂的时候使得两个子结点平衡); B树结点中还包含指向关键字具体信息的指针
            *   高度: h<=log\_t((n+1)/2)
            *   搜索: 多路搜索, B树根结点一直在内存, 而每一块新结点需要从磁盘读取
            *   插入: 如果要插入的结点慢, 则需要对其进行分裂操作, 将第t个元素上升到父节点(前t个保留在原结点, 后t个移到新生成的结点, 如B-TREE-SPLIT-CHILD式), 当然也要保证父节点非满, 所以当沿树往下查找关键字位置时, 就分裂沿途遇到的每一个满结点, 如此即可确保父节点非满.
            *   删除: 删除必须保证结点关键字的个数不小于t, 从根开始定位到k
                
                *   如果k不在内结点x中, 在其第i个子节点ci\[x\]中, 而ci\[x\]只有t-1个关键字
                
                1.  ci\[x\]有一个相邻兄弟结点包含至少t个关键字, 则将x中的关键字降到ci\[x\]中, 从中ci\[x\]的相邻的左/右兄弟的最大/小关键字上升到x中, 沿ci\[x\]继续定位
                2.  如果ci\[x\]翔哥相邻兄弟节点都包含t-1个关键字, 将ci\[x\]和一个兄弟节点合并,同时将x中的关键字降到合并后的结点中,继续
                
            
            *   如果定位到k在x结点x中
            
            1.  x是叶结点, 直接删除(有了1保证删除后结点不会过小); 
            2.  x是内结点, 且k左/右侧的子节点y/z包含至少t个关键字, 则找出k在以y/z为根的子树中的前驱/后继k', 递归删除k', 并在x中用k'取代k
            3.  x是内结点,且y和z都只包含t-1个关键字, 则将y和z合并,并删除k, 更新x
            
        2.  B+树
            *   结点中包含n个关键字和n个指针; 所有非终端结点=索引, 索引仅包含其子树根中最大(小)的关键字(多级索引); 相比B树, 其内结点不包含指向关键字具体信息的指针(如直线某条记录), 同样一个快可以存储更多的内容, 减少IO次数. 见图4
        3.  B\*树
            *   B+树的分裂和B树一样, 满则分成两个结点, 相当于空间利用率为1/2, 而B\*树则在每个内结点中接入一个指向相邻兄弟结点的指针, 当结点满时, 看兄弟结点是否满, 不满则复制一部分内容过去, 在插入新结点; 若满则创建一个新结点, 两边各复制1/3, 相当于空间利用率为2/3, 更饱满.
        4.  比较
            *   B树->有序表+平衡多叉树; B+树->有序数组链表+平衡多叉树; B\*树->更饱满的B+树
            *   B+树所有信息都存在叶结点, 所以其查找删除消耗稳定, IO少, 所以多用于数据库; B树相对B+树的好处是可以针对不同频率的查询, 将高频查询放到根结点,
        5.  R树
            1.  是B树在高维空间的扩展, R表示Rectangle, 将空间数据表示成矩形, 大矩形包含小矩形, 形成树.(矩形的生成很有讲究, 好好学)
    
    *   ![[Archive/面试资料/Programming/_resources/Tree_Problem.resources/unknown_filename.8.png]] ![[Archive/面试资料/Programming/_resources/Tree_Problem.resources/unknown_filename.6.png]] ![[Archive/面试资料/Programming/_resources/Tree_Problem.resources/unknown_filename.7.png]]
    *   ![[Archive/面试资料/Programming/_resources/Tree_Problem.resources/unknown_filename.9.png]]![[Archive/面试资料/Programming/_resources/Tree_Problem.resources/unknown_filename.10.png]]
    
    7.  Trie树
        1.      def search(self, trie, word, skip\_level=-1):
        2.          queue = deque(\[trie\])
        3.          for i, c in enumerate(word):
        4.              size = len(queue)
        5.              while size > 0:
        6.                  t = queue.popleft()
        7.                  if i == skip\_level:
        8.                      for n in t.values():
        9.                          queue.append(n)
        10.                  elif c in t:
        11.                      queue.append(t\[c\])
        12.                  size -= 1
        13.          return map(lambda t:t\['i'\], queue) # search trie tree, support broad match one level
        
        15.      def create\_trie(self, wordList):
        16.          trie = {}
        17.          for i,word in enumerate(wordList):
        18.              t = trie
        19.              for c in word:
        20.                  if c not in t: t\[c\] = {}
        21.                  t = t\[c\]
        22.              t\['i'\] = i # add index in leaf node
        23.          return trie
    
    *   ====Don’t use trie tree at first, usually string slice check in hash is very quick, e.g.==[concatenated-words](https://leetcode.com/problems/concatenated-words)==,== [palindrome-pairs](https://leetcode.com/problems/palindrome-pairs/description/)==, use trie tree for optimization====
    
    9.  ==segment tree==
        1.  There are two implementation versions
        2.  
    10.  哈弗曼树
        1.  [https://blog.csdn.net/ns\_code/article/details/19174553](https://blog.csdn.net/ns_code/article/details/19174553)



----

- Date: 2012-09-08
- Tags: #note #Interview/Programing 



