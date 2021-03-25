#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rocky Wayne 
# @Created       : 2020-04-20 21:42:33
# @Last Modified : 2020-04-20 21:42:33
# @Mail          : lostlorder@gamil.com
# @Version       : alpha-1.0


# 二叉搜索树中的两个节点被错误地交换。
#
#  请在不改变其结构的情况下，恢复这棵树。
#
#  示例 1:
#
#  输入: [1,3,null,null,2]
#
#    1
#   /
#  3
#   \
#    2
#
# 输出: [3,1,null,null,2]
#
#    3
#   /
#  1
#   \
#    2
#
#
#  示例 2:
#
#  输入: [3,1,4,null,null,2]
#
#   3
#  / \
# 1   4
#    /
#   2
#
# 输出: [2,1,4,null,null,3]
#
#   2
#  / \
# 1   4
#    /
#   3
#
#  进阶:
#
#
#  使用 O(n) 空间复杂度的解法很容易实现。
#  你能想出一个只使用常数空间的解决方案吗？
#
#  Related Topics 树 深度优先搜索
#  👍 250 👎 0
import copy
import math

import pytest

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
        x = y = pre = None

        cur = root
        while stack or cur:
            while cur:
                stack.append(cur)
                cur = cur.left
            cur = stack.pop()
            if pre and cur.val < pre.val:
                y = cur
                if x is None:
                    x = pre
                else:
                    break
            pre = cur
            cur = cur.right

        x.val, y.val = y.val, x.val


class Solution1:

    def recoverTree(self, root: TreeNode) -> None:
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


class Solution2:
    def recoverTree(self, root: TreeNode) -> None:

        first_node = None
        second_node = None
        pre_node = TreeNode(-math.inf)

        def in_order(node):
            nonlocal first_node, second_node, pre_node
            if not node:
                return
            in_order(node.left)
            if first_node is None and pre_node.val >= node.val:
                first_node = pre_node
            if first_node and pre_node.val >= node.val:
                second_node = node
            pre_node = node
            in_order(node.right)

        in_order(root)
        first_node.val, second_node.val = second_node.val, first_node.val


@pytest.mark.parametrize("kwargs,expected", [
    [dict(
        root=TreeNode(1,
                      left=TreeNode(3, right=TreeNode(2)))
    ),
        TreeNode(3,
                 left=TreeNode(1, right=TreeNode(2))
                 )
    ],

    [dict(
        root=TreeNode(3,
                      left=TreeNode(1),
                      right=TreeNode(4, left=TreeNode(2))
                      )
    ),
        TreeNode(2,
                 left=TreeNode(1),
                 right=TreeNode(4, left=TreeNode(3))
                 )
    ],

])
def test_solutions(kwargs, expected):
    root = kwargs["root"]
    root1 = copy.deepcopy(root)
    root2 = copy.deepcopy(root)
    Solution().recoverTree(root)
    Solution1().recoverTree(root1)
    Solution2().recoverTree(root2)
    assert repr(expected) == repr(root)
    assert repr(expected) == repr(root1)
    assert repr(expected) == repr(root2)


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=no", __file__])
