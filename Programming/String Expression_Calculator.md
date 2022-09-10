# String Expression/Calculator
----



1.  [evaluate-reverse-polish-notation](https://leetcode.com/problems/evaluate-reverse-polish-notation/description/): 给定波兰式表达式, 求算术值. 
    1.  \["2", "1", "+", "3", "\*”\] => 9
    2.  比较简单, 无需考虑优先级, 原地修改即可
2.  [score-of-parentheses](https://leetcode.com/problems/score-of-parentheses/description/):  给定字符串只包含’(‘, ‘)’, 以及计算规则, 求算术值. 
    1.  用stack maintain状态, 单遍扫描即可, 或者用递归形式
3.  [different-ways-to-add-parentheses](https://leetcode.com/problems/different-ways-to-add-parentheses/description/): 给定表达式字符串, 求添加括号得到不同算术值. 
    1.  采用递归的方式, 效率并不高.
    2.  dfs遍历表达式, 有括号的情况下, refer to [decode-string](https://leetcode.com/problems/decode-string)
    3.  ==构建表达式树==, #1中的扫描的第一层运算符即为根 https://blog.csdn.net/chenht8/article/details/53208914
4.  [Basic Calculator](https://leetcode.com/problems/basic-calculator): The expression string may contain open ( and closing parentheses ), the plus + or minus sign -, non-negative integers and empty spaces .
    
    *   example: (1+(4+5+2)-3)+(6+8)
    *   分析: 只有一种优先级, 即括号, +/-优先级相同, 可以采用如#3的dfs, 也可以用stack如#1
    
    1.  def calculate(self, s):
    2.      if not s: return 0
    3.  
    4.      stack = deque()
    5.      ans = 0
    6.      num, sign = 0, 1
    7.  
    8.      for i, ch in enumerate(s):
    9.          if ch.isdigit():
    10.              num = num \* 10 + int(ch)
    11.          elif ch == '+' or ch == '-':
    12.              ans += num \* sign
    13.              num = 0
    14.              sign = 1 if ch == '+' else -1
    15.          elif ch == '(':
    16.              stack.append(ans)
    17.              stack.append(sign)
    18.              # reset all parameters
    19.              num, sign = 0, 1
    20.              ans = 0
    21.          elif ch == ')':
    22.              ans += sign \* num
    23.              ans \*= stack.pop()  # pop out the sign before parenthesis
    24.              ans += stack.pop()  # pop out the number before parenthesis
    25.              num, sign = 0, 1
    26.  
    27.      if num > 0:
    28.          ans += sign \* num
    29.      return ans
5.  [Basic Calculator II](https://leetcode.com/problems/basic-calculator-ii): The expression string contains only non-negative integers, +, -, \*, / operators and empty spaces.
    
    *   Example: 3+5 / 2
    *   分析: 一种优先级, \*/优先于+-, 利用stack保存数字信息, 遇到\*/则直接计算
    
    1.  def calculate(self, s):
    2.      if not s: return 0
    3.  
    4.      stack = deque()
    5.      num, sign = 0, '+'
    6.      for i, ch in enumerate(s):
    7.          if ch.isdigit():
    8.              num = num \* 10 + int(ch)
    9.          if ch in '+-\*/' or i == len(s) - 1:
    10.              if sign == '+':
    11.                  stack.append(num)
    12.              elif sign == '-':
    13.                  stack.append(- num)
    14.              elif sign == '\*':
    15.                  stack.append(stack.pop() \* num)
    16.              elif sign == '/':
    17.                  stack.append(stack.pop() // num)
    18.              sign = ch
    19.              num = 0
    20.  
    21.      if num > 0:
    22.          stack.append(num)
    23.  
    24.      return sum(stack)
6.  [Basic Calculator III](https://leetcode.com/problems/basic-calculator-iii): The expression string contains only non-negative integers, +, -, \*, / operators , open ( and closing parentheses ) and empty spaces .
    1.  example: "(2+6\* 3+5- (3\*14/7+2)\*5)+3”
    2.  分析: 两种优先级, “()” > “\*/“ > “+-“, 用两个栈分别保存数字和操作, 还需要判断优先级次序, 如precedence
    3.  def calculate(self, s):
    4.      def operation(op, second, first):
    5.          if op == "+":
    6.              return first + second
    7.          elif op == "-":
    8.              return first - second
    9.          elif op == "\*":
    10.              return first \* second
    11.          elif op == "/":  # integer division
    12.              return first // second
    13.  
    14.      # calculate the relative precedence of the the operators "()" > "\*/" > "+="
    15.      # and determine if we want to do a pre-calculation in the stack
    16.      # (when current\_op is <= op\_from\_ops)
    17.      def precedence(current\_op, op\_from\_ops):
    18.          if op\_from\_ops == "(" or op\_from\_ops == ")":
    19.              return False
    20.          if (current\_op == "\*" or current\_op == "/") and (op\_from\_ops == "+" or op\_from\_ops == "-"):
    21.              return False
    22.          return True
    23.  
    24.      if not s: return 0
    25.      # define two stack: nums to store the numbers and ops to store the operators
    26.      nums, ops = \[\], \[\]
    27.      i = 0
    28.      while i < len(s):
    29.          c = s\[i\]
    30.          if c == " ":
    31.              i += 1
    32.              continue
    33.          elif c.isdigit():
    34.              num = int(c)
    35.              while i < len(s) - 1 and s\[i + 1\].isdigit():
    36.                  num = num \* 10 + int(s\[i + 1\])
    37.                  i += 1
    38.              nums.append(num)
    39.          elif c == "(":
    40.              ops.append(c)
    41.          elif c == ")":
    42.              # do the math when we encounter a ')' until '('
    43.              while ops\[-1\] != "(":
    44.                  nums.append(operation(ops.pop(), nums.pop(), nums.pop()))
    45.              ops.pop()
    46.          elif c in \["+", "-", "\*", "/"\]:
    47.              while len(ops) != 0 and precedence(c, ops\[-1\]):
    48.                  nums.append(operation(ops.pop(), nums.pop(), nums.pop()))
    49.              ops.append(c)
    50.          i += 1
    51.  
    52.      while len(ops) > 0:
    53.          nums.append(operation(ops.pop(), nums.pop(), nums.pop()))
    54.  
    55.      return nums.pop()
    56.  
7.  [Basic Calculator IV](https://leetcode.com/problems/basic-calculator-iv)



----

- Date: 2018-12-26
- Tags: #Interview/Programing 



