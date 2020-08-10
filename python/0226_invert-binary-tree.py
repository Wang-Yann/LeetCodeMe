#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-04-22 10:39:43
# @Last Modified : 2020-04-22 10:39:43
# @Mail          : rock@get.com.mm
# @Version       : alpha-1.0

# 翻转一棵二叉树。
#
#  示例：
#
#  输入：
#
#       4
#    /   \
#   2     7
#  / \   / \
# 1   3 6   9
#
#  输出：
#
#       4
#    /   \
#   7     2
#  / \   / \
# 9   6 3   1
#
#  备注:
# 这个问题是受到 Max Howell 的 原问题 启发的 ：
#
#  谷歌：我们90％的工程师使用您编写的软件(Homebrew)，但是您却无法在面试时在白板上写出翻转二叉树这道题，这太糟糕了。
#  Related Topics 树
#  👍 500 👎 0
import copy

import pytest

from common_utils import TreeNode


class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        if not root:
            return root
        left = self.invertTree(root.right)
        right = self.invertTree(root.left)
        root.left = left
        root.right = right
        return root


class Solution1:
    def invertTree(self, root: TreeNode) -> TreeNode:
        if not root:
            return root
        stack = [root]
        while stack:
            node = stack.pop()
            node.left, node.right = node.right, node.left
            if node.left:
                stack.append(node.left)
            if node.right:
                stack.append(node.right)
        return root


@pytest.mark.parametrize("kw,expected", [
    [dict(root=TreeNode(
        4,
        TreeNode(2, TreeNode(1), TreeNode(3)),
        TreeNode(7, TreeNode(6), TreeNode(9))
    )),
        TreeNode(
            4,
            TreeNode(7, TreeNode(9), TreeNode(6)),
            TreeNode(2, TreeNode(3), TreeNode(1)),
        )
    ],
])
def test_solutions(kw, expected):
    kw1 = copy.deepcopy(kw)
    assert repr(Solution().invertTree(**kw)) == repr(expected)
    assert repr(Solution1().invertTree(**kw1)) == repr(expected)


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=no", __file__])
