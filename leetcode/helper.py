
def rand(start=0, end=1, count=1000):
    import random
    return [random.randint(start,end) for _ in xrange(count)]
    
def rand_char(start=0, end=25, count=1000):
    import random
    a = ord('a')
    return [chr(a+random.randint(start,end)) for _ in xrange(count)]

def array2list(array):
    if not array or len(array) <= 0: return None

    head = ListNode(array[0])
    p = head
    for i in range(1, len(array)):
        p.next = ListNode(array[i])
        p = p.next
    return head

def list2array(head):
    array = []
    while head:
        array.append(head.val)
        head = head.next
    return array


class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

def array2tree(array):
    if len(array) <= 0 or array[0] == None: return None

    from collections import deque
    root = TreeNode(array[0])
    i, queue = 1, deque([root])
    while i < len(array):
        p = queue.popleft()

        if array[i] != None:
            p.left = TreeNode(array[i])
            queue.append(p.left)
        if i+1 < len(array) and array[i+1] != None:
            p.right = TreeNode(array[i+1])
            queue.append(p.right)

        i += 2
        
    return root

def tree2array(root):
    if root == None: return []

    ans, queue = [root.val], [root]
    head, tail = 0, len(queue)
    while head < len(queue):
        node = queue[head]
        head += 1

        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)
        
        if node.right or node.left:
            ans.append(node.left.val if node.left else None) 
            ans.append(node.right.val if node.right else None)
        if head == tail:
            tail = len(queue)
    if ans[-1] == None:
        ans.pop()
    return ans

def preorder(tree):
    if not tree: return

    ans, stack = [], []
    while tree or len(stack) > 0:
        while tree:
            ans.append(tree.val)
            stack.append(tree)
            tree = tree.left

        if len(stack) > 0:
            tree = stack.pop()
            tree = tree.right
    return ans

class UndirectedGraphNode:
    def __init__(self, x):
        self.label = x
        self.neighbors = []

def deserialize(s):
    # 0,1,2#1,2#2,2
    nodes = {}
    start = None
    arr = s.split('#')
    for val in arr:
        ns = val.split(',')
        if ns[0] not in nodes:
            nodes[ns[0]] = UndirectedGraphNode(ns[0])
        node = nodes[ns[0]]
        if not start: start = node
        for i in xrange(1, len(ns)):
            if ns[i] not in nodes:
                nodes[ns[i]] = UndirectedGraphNode(ns[i])
            node.neighbors.append(nodes[ns[i]])

    return nodes[start.label]

def serialize(graph):
    from collections import deque
    nodes = {graph.label:graph}
    queue = deque([graph])

    ans = []
    while len(queue) > 0:
        node = queue.popleft()
        ser = [node.label]
        for neighbor in node.neighbors:
            if neighbor.label not in nodes:
                nodes[neighbor.label] = neighbor
                queue.append(neighbor)
            ser.append(neighbor.label)
        ans.append(','.join(ser))
    return '#'.join(ans)




if __name__ == '__main__':
    print rand(0,100,300)
    print ''.join(rand_char(start=0, end=10, count=100))
    # arr=[1,2,3,4,5,6,7];assert tree2array(array2tree(arr)) == arr 
    # arr=[1,2,3,4,5,6,7,8];assert tree2array(array2tree(arr)) == arr 
    # arr=[1,2,None,3,None,4];assert tree2array(array2tree(arr)) == arr 
    
    # code=''; assert serialize(deserialize(code)) == code
    # code='0'; assert serialize(deserialize(code)) == code
    # code='0,1,2#1,2#2,2'; assert serialize(deserialize(code)) == code
    # code='0,1,2#1,2#2'; assert serialize(deserialize(code)) == code
    # code='0,1,2#1,2#2'; assert serialize(deserialize(code)) == code