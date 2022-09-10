# Graph Problem
----

1.  Graph Search
    
    1.  BFS(广度优先)和DFS(深度优先)是相对A\*是盲目的搜索方式, 适合搜索空间不大的问题; BFS用 FIFO Queue辅助搜索, DFS用FILO Stack辅助或Recursion搜索
    2.  A\*搜索采用启发式方法, 当前搜索结点往下选择下一步结点时，可以通过一个启发函数来进行选择, 选择代价最少的结点作为下一步搜索结点, 其核心估值函数f(n)=g(n)+h(n), 其中g(n)为从起始搜索点到当前点的代价, 如结点在搜索树中的深度; h(n)为当前结点到目标结点的估值. 当h(n)=0, 则A\*算法退化为Dijkstra单源路径搜索.
    3.  heuristics function h(n)需要满足如下条件才能使得搜索结果为最优, 保证f(n)为非减
        1.  admissibility: estimated heuristic costs <= actual cost, 反例如左下图
        2.  consistency: heuristic "arc" cost <= actual cost for each arc, 即h(A) - h(C) <= cost(A to C)
        3.  
        4.  ![[Archive/面试资料/Programming/_resources/Graph_Problem.resources/unknown_filename.17.png]]![[Archive/面试资料/Programming/_resources/Graph_Problem.resources/unknown_filename.18.png]]
    4.  [shortest-path-visiting-all-nodes](https://leetcode.com/problems/shortest-path-visiting-all-nodes): 不同于最小生成树, 此处搜索是连续的, 即A->B->A->C算三步, 依然是暴利搜索, 不过需要去重, 用bitmask很高效.
    
    1.  def shortestPathLength(self, graph):
    2.      queue = collections.deque()
    3.      visited = set()
    
    5.      for i in xrange(len(graph)):
    6.          bitmask = 1 << i
    7.          queue.append((i, bitmask, 0))   # start\_index, bitmask, cost
    8.          visited.add((i, bitmask))       # current\_index, bitmask
    
    10.      while queue:
    11.          index, bitmask, cost = queue.popleft()
    12.          # print index, bitmask, cost
    
    14.          # BFS guarantee the first one reach 2^N-1 is the shotest one
    15.          if bitmask == (1 << len(graph)) - 1:
    16.              return cost
    
    18.          for neighbor in graph\[index\]:
    19.              bm = bitmask | (1 << neighbor)
    20.              if (neighbor, bm) not in visited:
    21.                  visited.add((neighbor, bm))
    22.                  queue.append((neighbor, bm, cost+1))
    
2.  Minimum spanning tree (最小生成树)
    1.  最小生成树是一副连通加权无向图中一棵权值最小的生成树, 即最小生成树包含图的所有节点, 边权值最小的集合.
    2.  程序不断的从边集合中找出一条"安全边"加入最小生成树边集合A中, 如果边集合A的顶点全在S中, 且边(u, v)是通过割(S, V-S)权重最小的边, 则(u,v)是集合A的安全边.
    3.  Kruskal 
        1.  对所有边进行排序
        2.  贪心选择权重小的边 (u, v), 如果u, v不在一个集合中, 则加入边(u, v) 加入集合中A
            1.  维护一个结点集合, 以判断两个顶点是否均已加入集合A中
    
    *   O(ElgE) or O(ElgV) as |E| < |V|^2 
    
    5.  Prim
        1.  从任一顶点u出发, 加入到集合S
        2.  维护一个集合Q (heap) , 保存集合S到V-S的权重, 
        3.  每次从Q中取出权重最小的结点v, 加入S中, 并删除Q中与v相连的结点, 继续取直到Q为空
    
    *   O(E+VlgV): 遍历所有边为O(E), 维护集合Q (堆) 需要O(VlgV)
    
3.  Single-Source Shortest Path
    1.  Bellman-Ford: 能适应一般的情况, 即存在负权边的情况, O(|V|\*|E|)
        1.  从顶点s出发, 所以d\[s\] = 0, 其他节点d均为正无穷
        2.  采用DP的方式, 对每条边执行松弛操作, 共执行|V|轮
            *   松弛Relax: 对于图中的每条边, 如果起点 u 的距离 d 加上边的权值 w 小于终点 v 的距离 d，则更新终点 v 的距离值 d；
            *   if d\[v\] > d\[u\] + w(u, v), then d\[v\] = d\[u\] + w(w, v), 即三角不等式
        3.  最后检查是否存在负权回路, 遍历所有边(u, v), 如果d\[v\] > d\[u\] + w(u, v), 则说明存在负权回路.
    
    *   ![[Archive/面试资料/Programming/_resources/Graph_Problem.resources/unknown_filename.2.png]]
    
    3.  DAG-SHORTEST-PATHS: 针对有向无环图, 在Bellman-Ford算法的基础上加入拓扑排序, 可以避免BF盲目的松弛 O(V+E)
        1.  对图进行拓扑排序: topologically sort
        2.  按照拓扑顺序从s开始遍历后续节点u, 对所有(u,v), 松弛节点v
    
    *   对于拓扑排序在s之前以及部分后续节点, s不可达, 因此其权重为正无穷.
    *   ![[Archive/面试资料/Programming/_resources/Graph_Problem.resources/unknown_filename.png]]
    
    5.  Dijkstra: 针对有向无环图, 且所有边为非负权值.
        *   采用贪心算法, 类似BFS和Prim算法, 从集合Q中依次取出估值d\[u\]最小的结点u, 然后松弛其后继结点. 
        *   算法关键在于集合Q的维护, 用二叉/项堆,或斐波那契堆O(VlgV+E)
        *   ![[Archive/面试资料/Programming/_resources/Graph_Problem.resources/unknown_filename.1.png]]
        *   [cheapest-flights-within-k-stops](https://leetcode.com/problems/cheapest-flights-within-k-stops/description/)
            *   def findCheapestPrice(self, n, flights, src, dst, K):
            *       flyto = {}
            *       for f,t,w in flights:
            *           if f not in flyto: flyto\[f\] = \[\]
            *           flyto\[f\].append((t, w))
            *       if src not in flyto: return -1
            *   
            *       ans, queue = sys.maxint, \[(0, src, K)\]
            *       while len(queue) > 0:
            *    acc, f, c = heapq.heappop(queue) # use min heap to maintain Q
            *           if f not in flyto: continue
            *           for t, w in flyto\[f\]:
            *               if t == dst:
            *                   ans = min(ans, acc + w)
            *               elif c > 0 and acc + w < ans:
            *                   heapq.heappush(queue, (acc + w, t, c-1))
            *       return -1 if ans == sys.maxint else ans
    6.  One Pair Shortest Path: 可以通过单源最短路径方法解决, 或者A\*搜索.
4.  All Pairs Shortest Path
    1.  DP解决最短路径问题 (假设不存在负权回路)
        1.  设l^{m}\_{ij}表示顶点i到j的至多包含m条边,当m为0的时候, l^0\_ij = 0 if i=j else infinite
        2.  当m>0时, 存在最优子结构![[Archive/面试资料/Programming/_resources/Graph_Problem.resources/unknown_filename.4.png]]
            1.  从i到j用了m-1条边l^{m-1}\_{ik}
            2.  i->k用了m-1条边, 加上k->j的一条边
        3.  自底向上计算路径权值, 需要O(n^4)的时间复杂度 (i: 1->n, j:1->n, k:1->n, k到j的边最多可能有n-1条), n = |V|
    
    *   改进: 可采用类似矩阵乘法的重复平分的方式改进, L^(2m)=L^m\*L^m, O(n^3lgn), 详见<算法导论>
    
    3.  Floyd-Warshall O(n^3)
        *   顶点集V中的k个顶点子集{1,2,...,k}, 对V中任意顶点i,j, 设路径p是从i到j且中间结点全在集合{1,2,...,k}的最短路径, 假设k不在路径p上, 则p的所有顶点均在集合{1,2,...,k-1}; 如果k在路径p上, 则将路径k划分p1->k->p2, 如下图, 则所有结点均属于集合{1,2,...,k-1}. 
        *   ![[Archive/面试资料/Programming/_resources/Graph_Problem.resources/unknown_filename.3.png]]
        *   DP递归公式: 设d^k\_ij为从顶点i到j, 且满足所有中间顶点属于集合{1,2,...,k}的一条最短路径权值, D^n=(d^n\_ij)即为最终答案
            *   ![[Archive/面试资料/Programming/_resources/Graph_Problem.resources/unknown_filename.11.png]]
    4.  稀疏图上Johnson算法, O(V^2lgV+VE), 
        1.  如果图中所有边权值非负, 则以每个顶点为源点执行Dijkstra; 
        2.  如果G=(V,E)中有负权边但不含负权回路, 则采用重赋权技术, 再执行Dijkstra
            1.  在原图G外加入结点s, 初始化w(s, v) = 0, v是G中的所有点
            2.  利用Bellman-Ford方法检查是否存在负权回路, 同时得到d(v) or h(v)
            3.  进行重赋权: 设新的权重函数 w'(u, v) = w(u, v)+h(u)-h(v), 因为不存在负权回路, 所以w’(u,v)>=0满足三角不等式
            4.  最后对每个结点执行Dijkstra, 然后恢复"重赋权"
        3.  ![[Archive/面试资料/Programming/_resources/Graph_Problem.resources/unknown_filename.6.png]]![[Archive/面试资料/Programming/_resources/Graph_Problem.resources/unknown_filename.5.png]]
        4.  ![[Archive/面试资料/Programming/_resources/Graph_Problem.resources/unknown_filename.12.png]]
5.  Max-Flow Min-Cut: 
    1.  最大流是从源点s到汇点t的最多的流量, 分到多条路径上
    2.  Ford-Fulkerson
        1.  残留网络 (residual network): 残留容量c\_f(u,v)=容量c(u, v) - 流量 f(u, v), 则残留网络为E\_f{(u,v)|c\_f(u,v)>0}, 
            1.  a)是流网络G和流f, 边s->v1上的11/16表示流量/网络容量, 流量为0则不显示; 
            2.  b)为对应的残留网络, 从c(s, v1)=16, f(s, v1)=11, 则c\_f(s, v1)=5, c\_f(v1, s)=0-f(v1, s)=11, 
        2.  增广路径 (augmenting path): 是残留网络上从s到t的简单路径p, 比如b)中s->v2->v3->t, 在不违反边的容量限制条件下, 增广路径上的每条边(u, v)可以容纳从u到v的额外正网络流. c\_f(p)=min{c\_f(u, v): (u,v)在p上}
        3.  沿着增广路径反复增加流,  图c)为在a)的基础上加入c\_f(p), 如f(s, v2)从8/13变为12/13, f(v3, v2) = 0/9;
        4.  图d)为新得到的残留网络, 继续执行, 直到找不到新的增广路径. 因为一个流是最大流, 当前仅当其残留网络不包含增广路径(最大流最小割定理)
        5.  图d) 中, 割(S, T)的净流为f(v1,v3)+f(v2, v3)+f(v2, v4) = 19, 其中S = {s, v1, v2}, T = {v3, v4, t}
        6.  ![[Archive/面试资料/Programming/_resources/Graph_Problem.resources/unknown_filename.14.png]]![[Archive/面试资料/Programming/_resources/Graph_Problem.resources/unknown_filename.13.png]]
        7.  ==[Edmonds-Karp](https://brilliant.org/wiki/edmonds-karp-algorithm/)==
            1.  不算单独算法, 是Ford-Fulkerson的一种实现方法, FF的复杂度为O(E f\*), 其复杂度为O(V\*E^2), 与maximum flow f无关.
            2.  第4行可以采用广度优先所有来发现增广路径, 如果增广路径是残留网络中从s到t的最短路径(每条边为单位距离)
            3.  
            4.  def bfs(capacity, edges, resNet, s, t):   # BFS find a path from s to t and the minimum flow in this path
            5.   queue = collections.deque(\[(s, float('inf'), {})\])
            6.   while queue:
            7.   node, flow, path = queue.popleft()
            8.   if node == t:
            9.   return flow, path
            10.   for neighbor in edges\[node\]:
            11.   if neighbor in path: continue
            12.   newpath = path.copy()
            13.   f = capacity\[node\]\[neighbor\] - resNet\[node\]\[neighbor\]
            14.   if f > 0:
            15.   newpath\[neighbor\] = node
            16.   queue.append((neighbor, min(flow, f), newpath))
            17.   return 0, {}
            18.  
            19.  def ==EdmondsKarp==(capacity, s, t):
            20.   maxFlow = 0
            21.   resNet = \[\[0\]\*len(capacity) for \_ in xrange(len(capacity))\]
            22.  
            23.   edges = collections.defaultdict(list)
            24.   for i, row in enumerate(capacity):
            25.   for j, cap in enumerate(row):
            26.   if cap > 0: edges\[i\].append(j)
            27.  
            28.   while True:
            29.   pathFlow, path = bfs(capacity, edges, resNet, s, t)
            30.   # print pathFlow, path, resNet
            31.   if pathFlow == 0: break
            
            33.   maxFlow += pathFlow
            34.   cur = t
            35.   while cur != s:
            36.   prev = path\[cur\]
            37.   resNet\[prev\]\[cur\] += pathFlow    # flow from prev to cur
            38.   resNet\[cur\]\[prev\] -= pathFlow     # resident flow from cur to prev
            39.   cur = prev
            40.   return maxFlow
            41.  
            42.  capacity = \[\[0, 1000000, 1000000, 0\], \[0, 0, 1, 1000000\], \[0, 0, 0, 1000000\], \[0, 0, 0, 0\]\]
            43.  print EdmondsKarp(capacity, 0, 3) == 2000000
    3.  ==压入与重标记法(todo)==
        1.  溢出顶点u: 离开顶点u, 且未被充满的仅有管道所连接的顶点与u等高或高于u
        2.  重标记: 为了是溢出顶点u摆脱其余流, 必须增加它的高度, 将其高度设置为比起最低相邻顶点的高度+1
        3.  高度函数h(u): 保证每条残留网络上的边(u, v)有h(u)<=h(v)+1, 此公式可将h理解为离汇点t的距离, 满足三角不等式.
        4.  算法流程: \[过程可参考 http://wenku.baidu.com/view/bc2fe04733687e21af45a965.html\]
            *   初始化: h\[s\]=|V|, 其余为0, 从源点s开始按c(s, v)将流压入与其相连的v中, 更新f(s, v), e(v), e(s)等
            *   保持: 不断的找到溢出顶点, 并执行relabel和push操作, 直到没有可能的relabel和push操作
            *   终止: 此时V-{s, t}中每个顶点的余流必为0 \[有些回流到s中\]
        5.  ![[Archive/面试资料/Programming/_resources/Graph_Problem.resources/unknown_filename.8.png]]![[Archive/面试资料/Programming/_resources/Graph_Problem.resources/unknown_filename.7.png]]
6.  Bipartite Graph Matching: 
    1.  概念
        1.  二分图: 把一个图的顶点划分为两个不相交集 U 和V ，使得每一条边都分别连接U、V中的顶点
        2.  匹配(matching) 是一个边的集合，其中任意两条边都没有公共顶点
        3.  最大匹配：一个图所有匹配中，所含匹配边数最多的匹配
        4.  完美匹配：如果一个图的某个匹配中，所有的顶点都是匹配点
    2.  用最大流的方式解决, 添加一个源点s和汇点t, 从s到t的一个最大流即为图的二分匹配. 
        1.  ![[Archive/面试资料/Programming/_resources/Graph_Problem.resources/unknown_filename.15.png]]
    3.  匈牙利算法 (Hungarian): 针对无权二分图, refer to [here](https://www.renfei.org/blog/bipartite-matching.html)
        1.  交替路：从一个未匹配点出发，依次经过非匹配边、匹配边、非匹配边…形成的路径叫交替路。
        2.  增广路：从一个未匹配点出发，走交替路，如果途径另一个未匹配点（出发的点不算），则这条交替路称为增广路（agumenting path）
            1.  非匹配边比匹配边多一条, 只要把增广路中的匹配边和非匹配边的身份交换即可, 匹配边数目比原来多了 1 条
            2.  由于中间的匹配节点不存在其他相连的匹配边, 所以这样做不会破坏匹配的性质
        3.  匈牙利树: 从一个未匹配点出发运行 BFS, 走交替路直到到不能再扩展为止, 所有叶子节点均为匹配点.
        4.  
        5.  def preprocess(edges):
        6.   node = collections.defaultdict(set)
        7.   for v1, v2 in edges:
        8.   node\[v1\].add(v2)
        9.   node\[v2\].add(v1)
        10.   return node
        11.  
        12.  def hungarian\_dfs(edges):
        13.   node = preprocess(edges)
        14.   n, matching = len(node), \[-1\] \* n
        15.  
        16.   def dfs(x, visited):
        17.   for neighbor in node\[x\]:
        18.   if neighbor in visited: continue
        19.   visited.add(neighbor)
        20.   if matching\[neighbor\] == -1 or dfs(matching\[neighbor\], visited):
        21.   # not a match point
        22.   matching\[x\] = neighbor
        23.   matching\[neighbor\] = x
        24.   return True
        25.   return False
        26.  
        27.   ans = 0
        28.   for i in xrange(n):
        29.   if matching\[i\] != -1: continue
        30.   if dfs(i, set(\[i\])):
        31.   ans += 1
        32.  
        33.   return ans, matching
        34.  
        35.  def hungarian\_bfs(edges): \# similar to Hopcroft–Karp
        36.   node = preprocess(edges)
        37.   n = len(node)
        38.   matching = \[-1\] \* n
        39.   ans = 0
        40.   for i in xrange(n):
        41.   if matching\[i\] != -1: continue
        42.   queue = collections.deque(\[i\])
        43.   visited = set()
        44.   prev = {i:-1} # start point
        45.   found = False
        
        47.   while queue and not found:
        48.   x = queue.popleft()
        49.   for neighbor in node\[x\]:
        50.   if neighbor in visited: continue
        51.   visited.add(neighbor)
        
        53.   if matching\[neighbor\] != -1:
        54.   # x -> neighbor -> matching\[neighbor\]
        55.   prev\[matching\[neighbor\]\] = x
        56.   queue.append(matching\[neighbor\])
        57.   else:
        58.   # i to neighbor is a agumenting path
        59.   # flip matching edge
        60.   found = True
        61.   d, e = x, neighbor
        62.   while d != -1:  # end by i
        63.   t = matching\[d\]
        64.   matching\[d\], matching\[e\] = e, d
        65.   d = prev\[d\] # the one previous matching point
        66.   e = t       # try to flip another d -> e
        67.   break
        68.  
        69.   if matching\[i\] != -1: ans += 1
        70.   return ans, matching
    4.  Kuhn-Munkras (KM) algorithm - weighted bipartite graph matching. refer to [here](https://blog.csdn.net/sixdaycoder/article/details/47720471)
        1.  完备匹配: X中的每一个顶点都与Y中的一个顶点匹配; 最佳匹配: 带权二分图的权值最大的完备匹配.
        2.  可行顶标: 对原图的任意结点, 给定顶标函数L(node), lx(x)记录集合X的结点顶标值, ly(y)记录集合Y的结点顶标值
            1.  对于任意边edge (x,y)满足: lx(x) + ly(y) >= weight(x, y)   — (1)
        3.  可行边: 满足lx(x) + ly(y) = weight(x, y)的边
        4.  相等子图: 原图的一个生成子图, 即包含所有节点以及可行边
        5.  算法原理: 如果原图的一个相等子图中包含完备匹配, 则此匹配即为原图的最佳二分图匹配
            1.  证明: 由于算法中一直保持顶标的可行性, 所以任意一个匹配的权值之和肯定小于等于所有结点分顶标之和, 则相等子图中完备匹配肯定是最佳匹配.
            2.  由公式(1) 可得 ![[Archive/面试资料/Programming/_resources/Graph_Problem.resources/unknown_filename.16.png]], 而当一个匹配G\*的边权和恰好为K时, G\*即为最佳匹配.
        6.  KM算法的核心部分即控制修改可行顶标的策略使得最终可到达一个完美匹配
            1.  初始化lx(x)和ly(y), lx(i) = max(weight(i, \*)), ly(j) = 0, 其满足公式 (1)
            2.  初识状态下, 每个节点x都存在一条可行边, 如果这些可行边相互不冲突, 即不share同一个结点y, 当前可行边的匹配即为最佳匹配.
            3.  否则, 需要不断调整/降低lx(x)值, 使得所有lx(x)和ly(y)的和 = K, 即达到最佳匹配.
        7.  如何调整lx(x)? 
            1.  可以贪心扩展匈牙利算法, 在增广路上属于集合X的所有点减去常数delta, 属于集合Y的所有点加上常数delta, 如此可保持公式(1)的限制, 增广路径总是从集合X出发, 结束于集合X, 所以每次x多减少delta.
            2.  对于任意边edge(i, j)以及weight(i, j), 只需要调整如下#2, 
                1.  如果i和j都在增广路上, lx\[i\] - delta + ly\[j\] + delta = lx\[i\] + ly\[j\]保持不变, 满足(1)
                2.  如果i在增广路上, j不属于, lx\[i\] - delta + ly\[j\]的值减少, edge(i,j)原来不在相等子图中, 现在可能加入. (初识lx\[i\] + ly\[j\] >= weight\[i\]\[j\])
                3.  如果i不在增广路上, j属于, lx\[i\] + ly\[j\] + delta值增大, 方向弄错, 更不可能加入到相等子图中
                4.  如果i, j都不在增广路上, lx\[i\], ly\[j\] 无变化, 满足(1)
            3.  如何选取delta? delta = min(lx\[i\] + ly\[j\] - weight\[i\]\[j\]), where i 在增广路上, j不在增广路上.
                1.  delta = min(lx\[i\] + ly\[j\] - weight\[i\]\[j\]) = lx\[i\] + ly\[j\] - max(weight\[i\]\[j\])
                2.  lx\[i\] − delta + ly\[j\] = lx\[i\]− lx\[i\] − ly\[j\] + max(weight\[i\]\[j\]) + ly\[j\] = max(weight) >= weight\[i\]\[j\]
        8.  复杂度: O(n^4)
            1.  依次对每个x进行匈牙利算法查找, 选择可行边的y, 未匹配则匹配, 否则进入step 2
            2.  遍历所有增广路上的x, 和非增广路上的y, 计算delta
            3.  用delta更新增广路上的x和y.
        9.  O(n^3) 的优化是对Y顶点的松弛函数slack, slack\[j\]保存跟当前节点j相连的节点i的lx\[i\]+ly\[j\]−weight\[i\]\[j\]最小值, #2中求delta是只需枚举不在增广路上的Y即可. 
        10.  
        11.  def KM(X, Y, weight):
        12.   lx, ly, matching = {}, {}, {} # use dict, X/Y can be label
        13.   for x in X:
        14.   lx\[x\] = max(weight\[x\].values())
        15.   matching\[x\] = -1
        16.   for y in Y:
        17.   ly\[y\] = 0
        18.   matching\[y\] = -1
        
        20.   def findpath(x, visitX, visitY, slack): # extend from hungarian
        21.   visitX.add(x)
        22.   tempDelta = 0
        23.  
        24.   for y in Y:
        25.   if y in visitY: continue
        26.   tempDelta = lx\[x\] + ly\[y\] - weight\[x\].get(y, 0)
        27.   if tempDelta == 0:  # feasible edge
        28.   visitY.add(y)
        29.   if matching\[y\] == -1 or findpath(matching\[y\], visitX, visitY, slack):
        30.   matching\[y\] = x
        31.   matching\[x\] = y
        32.   return True
        33.   elif slack\[y\] > tempDelta: # x in agumenting path but y not, pre-calculate slack
        34.   slack\[y\] = tempDelta
        35.   return False
        36.  
        37.   for x in X:
        38.   slack = {y:sys.maxint for y in Y}
        39.   while True:
        40.   visitX = set()
        41.   visitY = set()
        42.   if findpath(x, visitX, visitY, slack):
        43.   break
        44.   else:
        45.   delta = sys.maxint
        46.   for j, s in filter(lambda (j,s): j not in visitY, slack.iteritems()):
        47.   delta = min(delta, s)
        
        49.   for x in filter(lambda x: x in visitX, X):
        50.   lx\[x\] -= delta
        51.   for y in Y:
        52.   if y in visitY:
        53.   ly\[y\] += delta
        54.   else:
        55.   slack\[y\] -= delta 
        56.   # slack\[j\] = min(lx\[i\] + ly\[j\] - w\[i\]\[j\])
        57.   # j is not in visitY, no change on ly\[j\], but lx\[i\] -= delta
        58.   return matching
        59.  
        60.  weight = ({0:{3:5,4:10,5:15,6:10}, 1:{3:5,4:10}, 2:{3:10,5:20,6:10}})
        61.  print KM(\[0,1,2\], \[3,4,5,6\], weight) == {0: 6, 1: 4, 2: 5, 3: -1, 4: 1, 5: 2, 6: 0}
7.  强连通分量: 有向图的一个强连通分量是一个最大顶点集合C, 其中C中的每一对顶点u和v相互可达
    1.  无向图: DFS即可, 也可以用union-find实现
    2.  Tarjan: [(](https://www.byvoid.com/zhs/blog/scc-tarjan)[详细介绍](https://www.byvoid.com/zhs/blog/scc-tarjan)) 
        
        *   定义DFN(u)为节点u搜索的次序编号，Low(u)为u或u的可达的在栈中的节点的最早次序编号.
        
        1.  Tarjan(u)
        2.  {
        3.      DFN\[u\]=Low\[u\]=++Index           // 为节点u设定次序编号和Low初值
        4.      Stack.push(u)                       
        5.      for each (u, v) in E         
        6.          if (v is not visted)  
        7.              Tarjan(v) 
        8.              Low\[u\] = min(Low\[u\], Low\[v\])     // 当前u和v在栈中追溯到的最早编号, 遇到了环的情况
        9.          else if (v in S) 
        10.              Low\[u\] = min(Low\[u\], DFN\[v\])    // v还在节点中, 则用DFN\[v\]为v入栈时的编号
        11.      if (DFN\[u\] == Low\[u\])                      // 如果节点u是强连通分量的根, 即u是第一个入栈的, 其连通节点v的Low\[v\] = DFN\[n\], 所以一直出不了栈, 直到返回到n
        12.          repeat
        13.              v = S.pop                  // 将v退栈，为该强连通分量中一个顶点
        14.              print v
        15.          until (u== v)
        16.  }
    3.  Kosaraju ([详细介绍](https://www.jianshu.com/p/83d780e2ae4b))
        
        *   ![[Archive/面试资料/Programming/_resources/Graph_Problem.resources/unknown_filename.10.png]]
        
        1.  两个强连通分支A\*和B\*, 如果从B\*节点开始DFS, 需要两次操作, 即对应两个SCC(如何证明?), 如果从A\*开始则一次就完成了, 所以问题可以变成如何定位B\*节点.
        2.  需要引入finished time, 即第一次DFS遍历时完成该节点遍历的编号, 即从节点v出发, 可达节点越多, 其finished time可能越大 (不重复遍历), 可比较A\*与B\*
        3.  逆序原图G成G’, 如此finished time越大在G’中越小, 因此先从这些节点开始进行第二次DFS遍历, 就能找到强连通分支
            1.  第一次DFS从A\*出发, A\*的finished time大, 如果从B\*出发, A\*的finished time同样大
            2.  第二次DFS直接从A\*开始, 即可找到2个SCC
            3.  对于多个scc情况同理
    4.  Gabow ([详细介绍](http://www.cppblog.com/sosi/archive/2010/09/27/127863.aspx))
        
        *   Tarjan算法的变形, T算法中用DFN和Low来标识scc的根, G算法中用第二个stack来获得, 基本思想都一样, 只是不需要频繁更新Low值
        
        1.  Gabow(u)
        2.  {
        3.      DFN\[u\]=++Index           // 为节点u设定次序编号
        4.      stack1.push(u)
        5.      stack2.push(u)             // 维护第二个栈
        6.      for each (u, v) in E         
        7.          if (v is not visted) 
        8.              Gabow(v) 
        9.          else if (v in stack1)  
        10.              while DFN\[stack2.top\] > DFN\[v\]      // 找到一个环, v可能是该scc的根节点, 持续出栈stack2直到v
        11.                  do  stack2.pop
        12.      if (u == stack2.top)         // 不断回溯, 当stack2 top为scc的根节点是, 即Tarjan中DFN\[u\] == Low\[u\], 则找到了一个scc
        13.          stack2.pop
        14.          repeat
        15.              v = stack1.pop
        16.              print v
        17.          until (u== v)
        18.  }
    5.  Count Components
        1.  def ==countComponents\_union\_find==(self, n, edges):
        2.      def find(seq, i):
        3.          while seq\[i\] != i:
        4.              seq\[i\] = seq\[seq\[i\]\]    # compression
        5.              i = seq\[i\]
        6.          return i
        7.  
        8.      seq = range(n)
        9.      for f, t in edges:
        10.          fi = find(seq, f)
        11.          ti = find(seq, t)
        12.          if fi != ti:
        13.              seq\[fi\] = ti        # union
        14.              n -= 1
        15.  
        16.      # one more step to make all nodes has same id
        17.      # for i in xrange(n):
        18.      #     find(seq, i)
        19.      # print seq
        20.      return n
        21.  
        22.  def ==countComponents\_dfs==(self, n, edges):
        23.      matrix = \[\[\] for \_ in xrange(n)\]
        24.      for f, t  in edges:
        25.          matrix\[f\].append(t)
        26.          matrix\[t\].append(f)
        27.  
        28.      count = 0
        29.      visited = \[False\] \* n
        30.      for u in xrange(n):
        31.          if visited\[u\] == False:
        32.              stack = \[u\]
        33.              while len(stack) > 0:
        34.                  u = stack.pop()
        35.                  visited\[u\] = True
        36.                  for v in matrix\[u\]:
        37.                      if not visited\[v\]:
        38.                          stack.append(v)
        39.              count += 1
        40.      print seq
        41.      return count
        42.  
        43.  def ==countComponents\_tarjan\_for\_directed\_graph==(self, n, edges):
        44.      matrix = \[\[\] for \_ in xrange(n)\]
        45.      for f, t  in edges:
        46.          matrix\[f\].append(t)
        47.          matrix\[t\].append(f)
        48.  
        49.      self.count = 0
        50.      self.seq = 0
        51.      self.stack = \[\]
        52.  
        53.      dfn = \[-1\] \* n
        54.      low = \[-1\] \* n
        55.      def tarjan(matrix, u, dfn, low):
        56.          self.seq += 1
        57.          dfn\[u\] = low\[u\] = self.seq  # dfn is the seq of node visited,
        58.                                      # low is the minimum seq node u can reach
        59.          self.stack.append(u)
        60.          for v in matrix\[u\]:
        61.              if dfn\[v\] == -1:                    # not visited
        62.                  tarjan(matrix, v, dfn, low)     # dfs and check the neighbor v
        63.                  low\[u\] = min(low\[u\], low\[v\])    # u can reach v, thus can reach minimum seq that v reaches.
        64.              elif v in self.stack:
        65.                  low\[u\] = min(low\[u\], dfn\[v\])    # u can reach to v and v is in stack, they're in same component
        66.                                                  # v was visited earlier and might have lower seq, update low\[u\]
        67.          if dfn\[u\] == low\[u\]:
        68.              self.count += 1
        69.              while self.stack.pop() != u: pass
        70.  
        71.      for i in xrange(n):
        72.          if dfn\[i\] == -1:
        73.              tarjan(matrix, i, dfn, low)
        74.  
        75.      return self.count
8.  拓扑排序
    1.  ![[Archive/面试资料/Programming/_resources/Graph_Problem.resources/unknown_filename.9.png]]
    2.  DFS:
        1.  维护一个栈以及visited列表, 按序号依次访问(更新visited列表)节点n, 递归访问n的子节点m, 等所有节点m(及其子节点)入栈后, 在入栈n
        2.  缺点: 无法维护非常合理的排序, 比如节点2, 8理应排名靠前, 但此种无法做到.
        3.  优点: 简单直观, 用visited来避免环的问题
        4.  L ← Empty list that will contain the sorted nodes
        5.  S ← Set of all nodes
        6.  for each node n in S do
        7.      visit(n)
        8.  function visit(node n)
        9.      if n has not been visited yet then
        10.          mark n as visited
        11.          for each node m with an edge from n to m do
        12.              visit(m)
        13.          add n to L
    3.  Kahn
        1.  如下伪代码所示, 扫描O(V+E)得到无入度集合S, 并通过删除相关边来持续更新集合S, 还可以用来检测环.
        2.  优点: 拓扑结果比较优美, 比如节点2和8排在靠前位置(取决于S选取策略), 比较符合直观感受
        3.  缺点: 需要不断删除边以及更新节点的入度信息.
        4.  (把无入度改成无出度, 本质还是一样的, 只是在删除边的时候变成从m to n)
        5.  L← Empty list that will contain the sorted elements
        6.  S ← Set of all nodes with no incoming edges
        7.  while S is non-empty do
        8.      remove a node n from S
        9.      insert n into L
        10.      foreach node m with an edge e from n to m do
        11.          remove edge e from the graph
        12.          if m has no other incoming edges then
        13.              insert m into S
        14.  if graph has edges then
        15.      return error (graph has at least onecycle)
        16.  else
        17.      return L (a topologically sorted order)
    4.  有向图环检测: DFS/BFS/Kahn
        1.  adj\_matrices = \[\[\] for \_ in xrange(numNodes)\]
        2.  indegree = \[0\] \* numNodes
        3.  for f,t in edges:
        4.      adjmatrices\[f\].append(t)
        5.      indegree\[t\] += 1
        6.  
        7.  visited = \[False\] \* numCourses
        8.  onpath = \[False\] \* numCourses
        9.  def ==dfs\_cycle==(adjmatrices, node, visited, onpath):
        10.      if visited\[node\]: return False
        11.  
        12.      onpath\[node\] = visited\[node\] = True
        13.      for neighbor in adjmatrices\[node\]:
        14.          if onpath\[neighbor\] || dfs\_cycle(neighbor):
        15.              return True
        16.      onpath\[node\] = False
        17.      return False
        18.  
        19.  def ==bfs\_cycle==(adjmatrices, indegree):
        20.      size = len(indegree)
        21.      for i in xrange(size):
        22.          for j in xrange(size):
        23.              if indegree\[j\] == 0: break
        24.          else:
        25.              return True # there is no j that indgree is 0
        26.          indegree\[j\] = -1 # to prevent visiting it again
        27.          for neighbor in adjmatrices\[j\]:
        28.              indegree\[neighbor\] -= 1
        29.      return False
        30.  
        31.  def ==kahn==(adjmatrices, indegree):
        32.      from collections import deque
        33.      noincoming = deque()
        34.      ans = \[\]
        35.      size = len(indegree)
        36.  
        37.      for i in xrange(size):
        38.          if indegree\[i\] == 0: noincoming.append(i)
        39.  
        40.      while len(noincoming) > 0:
        41.          node = noincoming.popleft()
        42.          ans.append(node)
        43.          for neighbor in adjmatrices\[node\]:
        44.              indegree\[neighbor\] -= 1
        45.              if indegree\[neighbor\] == 0:
        46.                  noincoming.append(neighbor)
        47.  
        48.      if len(ans) != size:
        49.          return 'error:graph has at least onecycle'
        50.      else:
        51.          return ans
9.  Graph Matching
    1.  Blossom Algorithm or Edmonds’ matching can be used on any [graph](https://brilliant.org/wiki/graphs/) to construct a [maximum matching](https://brilliant.org/wiki/matching). The blossom algorithm improves upon the [Hungarian algorithm](https://brilliant.org/wiki/hungarian-matching/) by shrinking cycles in the graph to reveal [augmenting paths](https://brilliant.org/wiki/matching-algorithms/#augmenting-paths). Additionally, the Hungarian algorithm only works on weighted [bipartite graphs](https://brilliant.org/wiki/bipartite-graph/).
    2.  refer to https://brilliant.org/wiki/blossom-algorithm/



----

- Date: 2012-09-07
- Tags: #note #Interview/Programing 
- Source URL: [](http://blog.csdn.net/v_JULY_v/article/details/6093380)



