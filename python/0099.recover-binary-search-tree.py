#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rocky Wayne 
# @Created       : 2020-04-20 21:42:33
# @Last Modified : 2020-04-20 21:42:33
# @Mail          : lostlorder@gamil.com
# @Version       : alpha-1.0

from common_utils import TreeNode


class Solution:

    def recoverTree(self, root: TreeNode):
        """ 按中序遍历树。遍历后的数组应该是几乎排序的列表，其中只有两个元素被交换。

        迭代顺序很简单：尽可能的向左走，然后向右走一步，重复一直到结束。
        若要找到交换的节点，就记录中序遍历中的最后一个节点 pred（即当前节点的前置节点），并与当前节点的值进行比较。
        如果当前节点的值小于前置节点 pred 的值，说明该节点是交换节点之一。
        交换的节点只有两个，因此在确定了第二个交换节点以后，可以终止遍历。


        """
        stack = []
        x = y = pred = None

        cur = root
        while stack or cur:
            while cur:
                stack.append(cur)
                cur = cur.left
            cur = stack.pop()
            if pred and cur.val < pred.val:
                y = cur
                if x is None:
                    x = pred
                else:
                    break
            pred = cur
            cur = cur.right

        x.val, y.val = y.val, x.val

    def recoverTreeMorris(self, root: TreeNode) -> None:
        """TODO
        MorrisTraversal
        """
        if root is None:
            return
        broken = [None, None]
        pre, cur = None, root
        while cur:
            if cur.left is None:
                self.detectBroken(broken, pre, cur)
                pre = cur
                cur = cur.right
            else:
                node = cur.left
                while node.right and node.right != cur:
                    node = node.right
                if node.right is None:
                    node.right = cur
                    cur = cur.left
                else:
                    self.detectBroken(broken, pre, cur)
                    node.right = None
                    pre = cur
                    cur = cur.right
        broken[0].val, broken[1].val = broken[1].val, broken[0].val
        return

    def detectBroken(self, broken, pre, cur):
        if pre and pre.val > cur.val:
            if broken[0] is None:
                broken[0] = pre
            broken[1] = cur


if __name__ == '__main__':
    sol = Solution()
    samples = [
        ([1, 3, 2], [(0, 1)], [(1, 2)]),
        # ([3, 1, 4, 2], [(0, 1), (2, 3)], [(0, 2)]),
    ]
    lists = [TreeNode.initTreeSimple(*x) for x in samples]
    print(lists)
    res = [sol.recoverTree(x) for x in lists]
    print(lists)
