#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rocky Wayne 
# @Created       : 2020-04-21 20:47:39
# @Last Modified : 2020-04-21 20:47:39
# @Mail          : lostlorder@gamil.com
# @Version       : alpha-1.0

# 给定一个二叉树，原地将它展开为一个单链表。
#
#
#
#  例如，给定二叉树
#
#      1
#    / \
#   2   5
#  / \   \
# 3   4   6
#
#  将其展开为：
#
#  1
#  \
#   2
#    \
#     3
#      \
#       4
#        \
#         5
#          \
#           6
#  Related Topics 树 深度优先搜索
#  👍 420 👎 0

import copy

import pytest

from common_utils import TreeNode


class Solution:

    def flatten(self, root: TreeNode) -> None:
        """
        TODO
        """

        def helper(node, list_head):
            if node:
                list_head = helper(node.right, list_head)
                list_head = helper(node.left, list_head)
                node.right = list_head
                node.left = None
                return node
            else:
                # print(node,list_head)
                return list_head

        helper(root, None)


#     draw a picture for understanding iterative process
#
#     1
#    / \
#   2   5
#  / \   \
# 3   4   6
# -----------
# pre = 5
# cur = 4
#
#     1
#    /
#   2
#  / \
# 3   4
#      \
#       5
#        \
#         6
# -----------
# pre = 4
# cur = 3
#
#     1
#    /
#   2
#  /
# 3
#  \
#   4
#    \
#     5
#      \
#       6
# -----------
# cur = 2
# pre = 3
#
#     1
#    /
#   2
#    \
#     3
#      \
#       4
#        \
#         5
#          \
#           6
# -----------
# cur = 1
# pre = 2
#
# 1
#  \
#   2
#    \
#     3
#      \
#       4
#        \
#         5
#          \
#           6
#
#

class Solution0:

    def __init__(self):
        self.prev = None

    def flatten(self, root: TreeNode) -> None:
        if root is None:
            return None
        if root:
            self.flatten(root.right)
            self.flatten(root.left)
            root.right = self.prev
            root.left = None
            self.prev = root


class Solution1:

    def flatten(self, root: TreeNode) -> None:
        """
        特殊的先序遍历，提前将右孩子保存到栈中，我们利用这种遍历方式就可以防止右孩子的丢失了。由于栈是先进后出，所以我们先将右节点入栈
        """
        if not root:
            return
        stack = [root]
        pre = None
        while stack:
            node = stack.pop()
            if pre:
                pre.right = node
                pre.left = None
            if node.right:
                stack.append(node.right)
            if node.left:
                stack.append(node.left)
            pre = node

class Solution2:
    def flatten(self, root: TreeNode) -> None:
        preorderList = list()

        def preorderTraversal(root: TreeNode):
            if root:
                preorderList.append(root)
                preorderTraversal(root.left)
                preorderTraversal(root.right)

        preorderTraversal(root)
        size = len(preorderList)
        for i in range(1, size):
            prev, curr = preorderList[i - 1], preorderList[i]
            prev.left = None
            prev.right = curr



@pytest.mark.parametrize("args,expected", [
    (
            TreeNode(
                1,
                left=TreeNode(2, TreeNode(3), TreeNode(4)),
                right=TreeNode(5, right=TreeNode(6))
            ),
            TreeNode(1, right=TreeNode(2, right=TreeNode(3, right=TreeNode(4, right=TreeNode(5, right=TreeNode(6)))))),

    ),
])
def test_solutions(args, expected):
    root = copy.deepcopy(args)
    root0 = copy.deepcopy(args)
    root1 = copy.deepcopy(args)
    Solution().flatten(root)
    Solution0().flatten(root0)
    Solution1().flatten(root1)
    assert repr(root) == repr(expected)
    assert repr(root0) == repr(expected)
    assert repr(root1) == repr(expected)


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=no", __file__])
