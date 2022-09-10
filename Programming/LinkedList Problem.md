# LinkedList Problem
----

1.  链表逆序
    1.  if not head or not head.next:
    2.      return head
    3.  prev , current = None,head
    4.  while current:
    5.      next = current.next
    6.      current.next = prev
    7.      prev = current
    8.      current = next
    9.  return prev
2.  链表交叉/环检测/环入口点
    
    1.  [linked-list-cycle](https://leetcode.com/problems/linked-list-cycle/description/)
    
    1.  [linked-list-cycle-ii](https://leetcode.com/problems/linked-list-cycle-ii/description/)
        1.  initNode = ListNode(None)
        2.  initNode.next = head
        3.  slow, fast = initNode, initNode
        4.  while fast and fast.next:
        5.   slow, fast = slow.next, fast.next.next
        6.      if slow == fast:
        7.          while initNode != slow:
        8.              initNode, slow = initNode.next, slow.next
        9.          return slow
        10.  return None
3.  单链表 中间元素
    1.  slow, fast = initNode, initNode
    2.  while fast and fast.next:
    3.      slow, fast = slow.next, fast.next.next
    4.  mid = slow
4.  单链表回文判断
    1.  定位中间位置, reverse后半段, 然后依次判断
5.  ==链表合并排序==
    *   依次合并k长度的list, k从1增大到n/2, 实现详见[listsort.c](https://www.chiark.greenend.org.uk/~sgtatham/algorithms/listsort.c)
6.  合并排序链表
    1.  两个: 两个指针
    2.  k个: 败者树
7.  删除元素问题
    1.  删除第k个元素: [Remove Nth Node From End of List](https://leetcode.com/problems/remove-nth-node-from-end-of-list), 考虑k大于链表长度情况
    2.  删除链表重复元素
8.  链表旋转
    1.  [rotate-list](https://leetcode.com/problems/rotate-list/description/): 从指定位置k旋转到头部, 需要考虑k大于链表长度情况
9.  [copy-list-with-random-pointer](https://leetcode.com/problems/copy-list-with-random-pointer): 复制链表, 每个节点有一个随机指针
    1.  O(1) space solution
        1.  copy node one by one, original node's next point to new node, new node’s next point to original node’s next
        2.  set random pointers for new nodes
        3.  reset next pointers
    2.  use a map to keep random pointer works, but O(n) space



----

- Date: 2018-12-29
- Tags: #Interview/Programing 



