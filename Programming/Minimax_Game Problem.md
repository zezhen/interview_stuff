# Minimax/Game Problem
----

Alpha-Beta Pruning
 ![[Archive/面试资料/Programming/_resources/Minimax_Game_Problem.resources/unknown_filename.png]]
Depth-limited search

1.  search only to a limited depth in the tree
2.  Replace terminal utilities with an evaluation function for non-terminal positions


Expectimax Search
![[Archive/面试资料/Programming/_resources/Minimax_Game_Problem.resources/unknown_filename.1.png]]
![[Archive/面试资料/Programming/_resources/Minimax_Game_Problem.resources/unknown_filename.2.png]]



1.  [guess-the-word](https://leetcode.com/problems/guess-the-word)(hard)
2.  [cat-and-mouse](https://leetcode.com/problems/cat-and-mouse/description/)(hard)
3.  [robot-room-cleaner](https://leetcode.com/problems/robot-room-cleaner) (hard)
    1.      def cleanRoom(self, robot):
    2.          self.dfs(robot, 0, 0, 0, 1, set())
    
    4.      def dfs(self, robot, x, y, direction\_x, direction\_y, visited):
    5.          robot.clean()
    6.          visited.add((x, y))
    
    8.          for k in range(4):
    9.              neighbor\_x = x + direction\_x
    10.              neighbor\_y = y + direction\_y
    11.              if (neighbor\_x, neighbor\_y) not in visited and robot.move():
    12.                  self.dfs(robot, neighbor\_x, neighbor\_y, direction\_x, direction\_y, visited)
    13.                  robot.turnLeft()    
    14.                  robot.turnLeft()       # turn back head to (x,y)
    15.                  robot.move()          #  move back to (x,y)
    16.                  robot.turnLeft()       
    17.                  robot.turnLeft()      # turn back head to neighbor as start
    18.              robot.turnLeft()
    19.              direction\_x, direction\_y = -direction\_y, direction\_x
4.  [guess-number-higher-or-lower-ii](https://leetcode.com/problems/guess-number-higher-or-lower-ii/description/): 猜数字, 1-n, 猜错需要付响应数字的钱, 求要赢所付的最少钱数.
    
    *   DP方法, 详细解释参见[Minimax](http://www.cnblogs.com/grandyang/p/5677550.html)
    *   [bbccyy1](https://leetcode.com/problems/guess-number-higher-or-lower-ii/discuss/84764/Simple-DP-solution-with-explanation~~): For each number x in range\[i~j\]
        *   we do: result\_when\_pick\_x = x + max{DP(\[i~x-1\]), DP(\[x+1, j\])}
        *   \--> // the max means whenever you choose a number, the feedback is always bad and therefore leads you to a worse branch.
        *   then we get DP(\[i~j\]) = min{xi, ... ,xj}
        *   \--> // this min makes sure that you are minimizing your cost.
    
    1.  public int getMoneyAmount(int n) {
    2.      int\[\]\[\] table = new int\[n+1\]\[n+1\];
    3.      for(int j=2; j<=n; j++){
    4.          for(int i=j-1; i>0; i--){
    5.              int globalMin = Integer.MAX\_VALUE;
    6.              for(int k=i+1; k<j; k++){
    7.                  int localMax = k + Math.max(table\[i\]\[k-1\], table\[k+1\]\[j\]);
    8.                  globalMin = Math.min(globalMin, localMax);
    9.              }
    10.              table\[i\]\[j\] = i+1==j?i:globalMin;
    11.          }
    12.      }
    13.      return table\[1\]\[n\];
    14.  }
5.  [flip-game-ii](https://leetcode.com/problems/flip-game-ii): 给定只包含’+’的字符串, 每次flip将’++’变成’--‘, 最后一个不能再flip的人输, 检查先手是够保证能赢.
    1.  (刚开始尝试递归但思路错了, 也是尴尬) 如下方法, 递归+memo, 更进一步优化有[Stefan](https://leetcode.com/problems/flip-game-ii/discuss/73958/memoization-3150ms-130ms-44ms-python)以及[stellari](https://leetcode.com/problems/flip-game-ii/discuss/73954/Theory-matters-from-Backtracking(128ms)-to-DP-(0ms))
    2.  def canWin(self, s):
    3.      memo = {}
    4.      def can(s):
    5.          if s not in memo:
    6.              memo\[s\] = any(s\[i:i+2\] == '++' and not can(s\[:i\] + '-' + s\[i+2:\])
    7.                            for i in range(len(s)))
    8.          return memo\[s\]
    9.      return can(s)
    10.  
    11.  int len;
    12.  string ss;
    13.  bool canWin(string s) {
    14.      len = s.size();
    15.      ss = s;
    16.      return canWin();
    17.  }
    18.  bool canWin() {
    19.      for (int is = 0; is <= len-2; ++is) {
    20.          if (ss\[is\] == '+' && ss\[is+1\] == '+') {
    21.              ss\[is\] = '-'; ss\[is+1\] = '-';
    22.              bool wins = !canWin();
    23.              ss\[is\] = '+'; ss\[is+1\] = '+';
    24.              if (wins) return true;
    25.          }
    26.      }
    27.      return false;
    28.  }
6.  [can-i-win](https://leetcode.com/problems/can-i-win/description/): 两人依次从1-n中选择一个数, 第一个人累积和超过n为赢.
    *   思路与flip-game-ii一样, 递归+memo
7.  [predict-the-winner](https://leetcode.com/problems/predict-the-winner): 两人依次从数组两端选数, 最后得分多者胜.
    1.  思路类似, 递归+memo, 不过实现上刚开始自己的coding比较差.
    2.  def PredictTheWinner(self, nums):
    3.      total = sum(nums)
    4.      memo = {}
    5.  
    6.      def predict( nums, start, end, is\_first, memo):
    7.          if (start, end, is\_first) in memo:
    8.              return memo\[(start, end, is\_first)\]
    9.          if start > end:
    10.              return 0
    11.          if is\_first:
    12.              # max the result for player 1
    13.              result = max(
    14.                  nums\[start\] + predict(nums, start+1, end, not is\_first, memo),
    15.                  nums\[end\] + predict(nums, start, end-1, not is\_first, memo)
    16.              )
    17.          else:
    18.              # min the result for player 2
    19.              result = min(
    20.                  predict(nums, start+1, end, not is\_first, memo),
    21.                  predict(nums, start, end-1, not is\_first, memo)
    22.              )
    23.          memo\[(start, end, is\_first)\] = result
    24.          return result
    25.  
    26.  
    27.      score = predict(nums, 0, len(nums)-1, True, memo)
    28.      return score >= total / float(2)



----

- Date: 2018-12-28
- Tags: #Interview/Programing 



