import operator

class STNode:
    def __init__(self, start, end):
        self.start = start
        self.end = end
        self.value = 0
        self.left = None
        self.right = None

class SegmentTree(object):
    def __init__(self, nums):
        
        def _build(nums, start, end):
            root = STNode(start, end)
            if start == end:
                root.value = nums[start]
            else:
                mid = start + (end - start) // 2

                root.left = _build(nums, start, mid)
                root.right = _build(nums, mid+1, end)
                root.value = root.left.value + root.right.value

            return root

        self.tree = _build(nums, 0, len(nums)-1)

    def update(self, i, val):

        def _update(root, i, val):
            if root.start == root.end:
                root.value = val
            else:
                mid = root.start + (root.end - root.start) // 2
                if i <= mid:
                    _update(root.left, i, val)
                else:
                    _update(root.right, i, val)
                root.value = root.left.value + root.right.value

        _update(self.tree, i, val)

    def sumRange(self, i, j):

        def _sumRange(root, start, end):
            if start == end and root.start == root.end:
                return root.value

            mid = root.start + (root.end - root.start) // 2
            if end <= mid:
                return _sumRange(root.left, start, end)
            elif mid + 1 <= start:
                return _sumRange(root.right, start, end)
            else:
                return _sumRange(root.left, start, mid) + \
                    _sumRange(root.right, mid+1, end)

        return _sumRange(self.tree, i, j)


if __name__ == '__main__':
    nums = range(1,13)
    tree = SegmentTree(nums)

    def verify():
        for i in xrange(len(nums)):
            for j in xrange(i, len(nums)):
                assert tree.sumRange(i, j) == sum(nums[i:j+1])

    verify()
    tree.update(5, 10)
    nums[5] = 10
    verify()